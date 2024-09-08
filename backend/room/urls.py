from django.urls import path,include
from .views import RoomViewSet
from rest_framework.routers import DefaultRouter
app_name= "room"

router = DefaultRouter()
router.register(r'', RoomViewSet, basename='rooms')

urlpatterns = [
    path('', include(router.urls)),
]
