from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('gallery.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
     # path('comments/', include('comments.urls')),  # Закомментируйте или удалите эту строку
    path('moderation/', include('moderation.urls', namespace='moderation')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
