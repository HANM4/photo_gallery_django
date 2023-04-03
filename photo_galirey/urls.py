from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('gallery/', gallery, name='gallery'),
    path('gallery/<int:gallery_id>/', gallery_int, name='gallery_int'),
    path('review/<int:review_id>/', review_int, name='review_int'),
    path('review/', review, name='review'),
    path('contacts/', contacts, name='contacts'),
    path('gallery/hashtags/<int:hashtags_id>/', show_hashtags, name='hashtag'),
]