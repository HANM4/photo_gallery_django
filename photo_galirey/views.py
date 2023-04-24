from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, JsonResponse
from .models import *
from .business_logic import *
from .forms import *
from django.core.paginator import Paginator

hashtags_name_db = HashtagsName.objects.all()
hashtags_db = Hashtags.objects.all()
gallery_db = Gallery.objects.all()
imgs_gallery_db = Img.objects.all()
services_db = Services.objects.all()
specifics_services_db = SpecificsServices.objects.all()
faq_db = FAQ.objects.all()
review_db = Review.objects.all()
email_users_bd = EmailSendUsers.objects.all()


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
            call = request.POST.get('call')
            name = request.POST.get('name')
            message = request.POST.get('message')
            print(call)
            print(name)
            print(message)
            try:
                order_call_form.save()
                messeg = f'Уведомление!!! Новый заказ звонка был сохранен в админ панель.\nНомер телефона:{call}\nИмя:{name}\nСообщение:{message}'
                for i in email_users_bd:
                    send_email_of_site(i.from_email, i.to_email, messeg.encode('utf-8'), i.password, i.smtp_host)
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
            name_reviewer = request.POST.get('name_reviewer')
            social_networks = request.POST.get('social_networks')
            review = request.POST.get('review')
            gallery = request.POST.get('gallery')
            print(name_reviewer)
            print(social_networks)
            print(review)
            print(gallery)
            try:
                write_review_form.save()
                messeg = f'Уведомление!!! Новый отзыв был сохранен в админ панель.\nИмя:{name_reviewer}\nОтзыв:{review}\nСсылка на соцсеть для связи:{social_networks}\nКод услуги:{gallery}'
                for i in email_users_bd:
                    send_email_of_site(i.from_email, i.to_email, messeg.encode('utf-8'), i.password, i.smtp_host)
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
            call = request.POST.get('call')
            service = request.POST.get('service')
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            print(call)
            print(service)
            print(name)
            print(email)
            print(message)
            try:
                order_service_form.save()
                messeg = f'Уведомление!!! Новая заказанная услуга была сохранена в админ панель.\nИмя:{name}\nEmail:{email}\nНомер телефона:{call}\nКод услуги:{service}\nСообщение: {message}'
                for i in email_users_bd:
                    send_email_of_site(i.from_email, i.to_email, messeg.encode('utf-8'), i.password, i.smtp_host)
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
    paginator = Paginator(gallery_db, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        "page_obj": page_obj,
        "hashtags_name": hashtags_name_db,
        "gallery": gallery_db,
        "menu_activ": "Портфолио",
        "menu": MENU,
        "hashtags_selected_id": 0
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


def show_hashtags(request, hashtags_id):
    show_hashtag_pk = get_object_or_404(hashtags_name_db, pk=hashtags_id)

    hashtags = hashtags_db.filter(hashtag=hashtags_id)

    paginator = Paginator(hashtags, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        "page_obj": page_obj,
        "hashtags_name": hashtags_name_db,
        "hashtags": hashtags_db.filter(hashtag=hashtags_id),
        "hashtags_selected_id": hashtags_id,
        "menu_activ": "Портфолио",
        "menu": MENU
    }
    data["page_name"] = data["menu"][data["menu_activ"]]
    return render(request, 'photo_galirey/galirey.html', context=data)
