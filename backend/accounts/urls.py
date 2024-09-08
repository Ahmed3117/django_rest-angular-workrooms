# from . import views
# from django.contrib.auth import views as auth_views
# from django.urls import include, path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .views import RegisterView, ChangePasswordView, UpdateProfileView

# app_name = 'accounts'

# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet

# router = DefaultRouter()
# router.register(r'users', UserViewSet)


# urlpatterns=[
#     path('', include(router.urls)),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('change-password/', ChangePasswordView.as_view(), name='change_password'),
#     path('update-profile/', UpdateProfileView.as_view(), name='update_profile'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

# ]

################################################################
# newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
# accounts/urls.py

from django.urls import path
from .views import CreateUserView, RegisterView, LoginView, LogoutView, ChangePasswordView, UserDetailView, UserListView, UserProfileView
app_name = 'accounts'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('create-user/', CreateUserView.as_view(), name='create_user'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),  # Add this line

]
