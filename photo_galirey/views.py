from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, JsonResponse
from .models import *
from .forms import *

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


# обработчик ответа от формы заказа звонка
def order_call_answer(request):
    order_call_form = OrderCallForm()
    if request.method == 'POST':
        order_call_form = OrderCallForm(request.POST)
        if order_call_form.is_valid():
            print(request.POST.get('call'))
            print(request.POST.get('name'))
            print(request.POST.get('message'))
            try:
                order_call_form.save()
            except:
                order_call_form.add_error(None, 'Данные не были добавлены в БД')
                print(order_call_form.errors)
        else:
            print(order_call_form.errors)
    return order_call_form


# обработчик ответа от формы оставить отзыв
def write_review_form_answer(request):
    write_review_form = WriteReviewForm()
    if request.method == 'POST':
        write_review_form = WriteReviewForm(request.POST)
        if write_review_form.is_valid():
            print(request.POST.get('name_reviewer'))
            print(request.POST.get('social_networks'))
            print(request.POST.get('review'))
            print(request.POST.get('gallery'))
            try:
                write_review_form.save()
            except:
                write_review_form.add_error(None, 'Данные не были добавлены в БД')
                print(write_review_form.errors)
        else:
            print(write_review_form.errors)
    return write_review_form


# обработчик ответа от формы оставить отзыв
def order_service_form_answer(request):
    order_service_form = OrderServiceForm()
    if request.method == 'POST':
        order_service_form = OrderServiceForm(request.POST)
        if order_service_form.is_valid():
            print(request.POST.get('call'))
            print(request.POST.get('service'))
            print(request.POST.get('name'))
            print(request.POST.get('email'))
            print(request.POST.get('message'))
            try:
                order_service_form.save()
            except:
                order_service_form.add_error(None, 'Данные не были добавлены в БД')
                print(order_service_form.errors)
        else:
            print(order_service_form.errors)
    return order_service_form


def index(request):
    order_service_form = order_service_form_answer(request)
    data = {
        "order_service_form": order_service_form,
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
    write_review_form = write_review_form_answer(request)
    data = {
        "write_review_form": write_review_form,
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
    order_call_form = order_call_answer(request)
    data = {
        "order_call_form": order_call_form,
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
