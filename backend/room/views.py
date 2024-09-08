from rest_framework import viewsets, mixins
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import RoomSerializer
from .models import Room
from rest_framework import status
from django.db.models import Q

from rest_framework.pagination import PageNumberPagination

class RoomPagination(PageNumberPagination):
    page_size = 3

# class RoomViewSet(viewsets.ModelViewSet):
class RoomViewSet(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    serializer_class = RoomSerializer
    pagination_class = RoomPagination

    def get_queryset(self):
        # queryset =  Room.objects.filter(members=self.request.user.id)
        queryset = Room.objects.all()
        # if self.request.user.is_superuser == False:
        #     queryset =  Room.objects.filter(members=self.request.user)
        
        # Get the 'is_done' query parameter from the URL
        is_done = self.request.query_params.get('is_done')
        searchvalue = self.request.query_params.get('searchvalue')
        
        if is_done is not None:
            if is_done.lower() == 'true' :
                queryset = queryset.filter(is_done=True)
            elif is_done.lower() == 'false' :
                queryset = queryset.filter(is_done=False)
                
        if searchvalue is not None:
            queryset = queryset.filter(
                Q(title__icontains=searchvalue) | 
                Q(room_id__icontains=searchvalue)
            )

        return queryset
    def perform_create(self, serializer):
        room = serializer.save()
        room.is_done = False # set it as false even if it sent as true in create 
        if room.admin is None and room.members.exists():
            room.admin = room.members.first()
            room.save()

    def update(self, request, *args, **kwargs):
        room = self.get_object()
        serializer = self.get_serializer(room, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if room.admin is None and room.members.exists():
            room.admin = room.members.first()
        if self.request.user == room.admin:
            room.is_done = serializer.validated_data.get('is_done', room.is_done)
        
        # Remove 'is_done' from the validated data
        serializer.validated_data.pop('is_done', None)

        serializer.save() # save all fields except is_done
        room.save()

        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def join_room(self, request, pk):
        room = Room.objects.get(pk=pk)
        room_id = request.data.get('room_id')
        if room.room_id == room_id:
            room.members.add(request.user)
            room.save()
            return Response({"message": "User added to the room successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid room_id"}, status=status.HTTP_400_BAD_REQUEST)




