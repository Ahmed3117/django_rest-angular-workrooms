
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls',namespace='accounts')),
    path('api/rooms/', include('room.urls',namespace='room')),
    path('api/todos/', include('todo.urls',namespace='todo')),
    # path('chat/', include('chat.urls',namespace='chat')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
