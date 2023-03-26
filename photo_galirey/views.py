from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from .models import *

hashtags_name_db = HashtagsName.objects.all()
gallery_db = Gallery.objects.all()
imgs_gallery_db = Img.objects.all()
services_db = Services.objects.all()
specifics_services_db = SpecificsServices.objects.all()
faq_db = FAQ.objects.all()
review_db = Review.objects.all()

MENU = {
    'Главная': 'home',
    'Портфолио': 'gallery',
    'Контакты': 'contacts',
    'Отзывы': 'review'
}


def index(request):
    data = {
        "menu_activ": "Главная",
        "menu": MENU,
        "specifics_services": specifics_services_db,
        "services": services_db,
        "faq": faq_db
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
    return render(request, 'photo_galirey/galirey.html', context=data)


def gallery_int(request, gallery_id):
    gallery_pk = get_object_or_404(gallery_db, pk=gallery_id)
    data = {
        "menu_activ": "Портфолио",
        "menu": MENU,
        "gallery_int": gallery_pk,
        "review": review_db.filter(pk=gallery_id).first(),
        "imgs_gallery": imgs_gallery_db.filter(gallery=gallery_id)
    }
    data["page_name"] = data["menu"][data["menu_activ"]]
    return render(request, 'photo_galirey/gallery_int.html', context=data)


def review(request):
    data = {
        "menu_activ": "Отзывы",
        "menu": MENU,
        "review": review_db
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


def page_not_found(request, exception):
    data = {
        "hashtags_name": hashtags_name_db,
        "gallery": gallery_db,
        "menu_activ": "gallery",
        "menu": MENU
    }
    return HttpResponseNotFound('404')


def review_int(request, review_id):
    review_pk = get_object_or_404(review_db, pk=review_id)
    data = {
        "menu_activ": "Отзывы",
        "menu": MENU,
        "review_int": review_pk,
        "gallery": gallery_db.get(pk=review_id)
    }
    data["page_name"] = data["menu"][data["menu_activ"]]
    return render(request, 'photo_galirey/review_int.html', context=data)
