from django.urls import path
from . import views
from .views import delete_photo
app_name = 'gallery'
urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_photo, name='upload'),
    path('photo/<int:pk>/', views.view_photo, name='photo_detail'),
    path('photo/<int:pk>/like/', views.like_photo, name='like_photo'),
    path('photo/delete/<int:photo_id>/', delete_photo, name='delete_photo'),
]
