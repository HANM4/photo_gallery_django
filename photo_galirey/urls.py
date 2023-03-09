from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('gallery/', gallery, name='gallery'),
    path('gallery_<int:gallery_id>/', gallery_int, name='gallery_int'),
    path('review/', review, name='review'),
    path('contacts/', contacts, name='contacts'),
]