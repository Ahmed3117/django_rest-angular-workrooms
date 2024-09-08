# # views functions that i created in model
# from rest_framework import status
# from rest_framework.response import Response


# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.generics import CreateAPIView, UpdateAPIView
# from django.contrib.auth import get_user_model

# from .serializers import RegisterSerializer, ChangePasswordSerializer, UpdateProfileSerializer
# from django.contrib.auth import authenticate
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework import viewsets
# from .serializers import UserSerializer
# # from .tokens import create_jwt_pair_for_user
# User = get_user_model()
# from rest_framework import permissions

# class RegisterView(CreateAPIView):
#     serializer_class = RegisterSerializer
#     permission_classes = []

#     def post(self, request):
#         data = request.data
#         serializer = self.serializer_class(data=data)
#         if serializer.is_valid():
#             account = serializer.save()
#             data = serializer.data
#             response = {"message": "User Created Successfully", "data": data}

#             return Response(data=response, status=status.HTTP_201_CREATED)

#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ChangePasswordView(UpdateAPIView):
#     serializer_class = ChangePasswordSerializer

#     def update(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = request.user
#         user.set_password(serializer.validated_data.get("new_password"))
#         user.save()
#         return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)


# class UpdateProfileView(UpdateAPIView):
#     serializer_class = UpdateProfileSerializer

#     def update(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = request.user
#         user.name = serializer.validated_data.get("new_name")
#         user.email = serializer.validated_data.get("new_email")
#         user.image = serializer.validated_data.get("new_image")
#         user.save()
#         return Response({"message": "Profile updated successfully"}, status=status.HTTP_200_OK)


# ################################################################
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer




#########################################################################################
# newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
# accounts/views.py

# accounts/views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer  # Import this
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateUserSerializer, ProfileSerializer, UserSerializer, RegisterSerializer, ChangePasswordSerializer
from rest_framework.parsers import MultiPartParser, FormParser
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    parser_classes = [MultiPartParser, FormParser]


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = TokenObtainPairSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
        
        
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
