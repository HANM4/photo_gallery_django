from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import *

hashtags_name_db = HashtagsName.objects.all()
gallery_db = Gallery.objects.all()
imgs_gallery_db = Img.objects.all()

MENU = {
    'Главная': 'home',
    'Портфолио': 'gallery',
    'Контакты': 'contacts',
    'Отзывы': 'review'
}


def index(request):
    data = {
        "menu_activ": "Главная",
        "menu": MENU
    }
    return render(request, 'photo_galirey/index.html', context=data)


def gallery(request):

    data = {
        "hashtags_name": hashtags_name_db,
        "gallery": gallery_db,
        "menu_activ": "Портфолио",
        "menu": MENU
    }
    data["page_name"] = data["menu"][data["menu_activ"]]
    print(data)
    return render(request, 'photo_galirey/galirey.html', context=data)


def gallery_int(request, gallery_id):
    data = {
        "menu_activ": "Портфолио",
        "menu": MENU,
        "gallery": gallery_db.get(pk=gallery_id),
        "imgs_gallery": imgs_gallery_db.filter(gallery=gallery_id)
    }
    data["page_name"] = data["menu"][data["menu_activ"]]
    return render(request, 'photo_galirey/gallery_int.html', context=data)


def review(request):
    data = {
        "menu_activ": "Отзывы",
        "menu": MENU
    }
    data["page_name"] = data["menu"][data["menu_activ"]]
    return render(request, 'photo_galirey/review.html', context=data)


def contacts(request):
    data = {
        "menu_activ": "Контакты",
        "menu": MENU
    }
    data["page_name"] = data["menu"][data["menu_activ"]]
    return render(request, 'photo_galirey/contacts.html', context=data)


def pageNotFound(request, exception):
    data = {
        "hashtags_name": hashtags_name_db,
        "gallery": gallery_db,
        "menu_activ": "gallery",
        "menu": MENU
    }
    return HttpResponseNotFound('404')