from rest_framework import viewsets

from .serializers import TodoSerializer

from .models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        room_id = self.request.query_params.get('room')
        if room_id:
            return Todo.objects.filter(room_id=room_id)
        return super().get_queryset()
