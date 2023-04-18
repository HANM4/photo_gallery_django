from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_work', 'get_html_a_img_background_work', 'publication', 'date_creation', 'date_changes')
    list_display_links = ('id', 'name_work')
    search_fields = ('id',)
    list_editable = ('publication',)
    fields = ('name_work', ('img_background_work', 'get_html_img_background_work'), 'publication',  'date_creation', 'date_changes')
    readonly_fields = ('get_html_img_background_work',  'date_creation', 'date_changes')

    def get_html_a_img_background_work(self, object):
        if object.img_background_work:
            return mark_safe(f"<img src='{object.img_background_work.url}' width=50> <a href='{object.img_background_work.url}'>{object.img_background_work}</a>")

    def get_html_img_background_work(self, object):
        if object.img_background_work:
            return mark_safe(
                f"<img src='{object.img_background_work.url}' width=50>")

    get_html_img_background_work.short_description = 'Изображение на данный момент'
    get_html_a_img_background_work.short_description = 'Обложка альбома'


class ImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery', 'get_html_a_img', 'date_creation', 'date_changes')
    list_display_links = ('id',)
    search_fields = ('gallery',)
    list_filter = ('gallery',)
    fields = ('gallery', ('img', 'get_html_img'), 'date_creation', 'date_changes')
    readonly_fields = ('get_html_img', 'date_creation', 'date_changes')

    def get_html_a_img(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=50> <a href='{object.img.url}'>{object.img}</a>")

    def get_html_img(self, object):
        if object.img:
            return mark_safe(
                f"<img src='{object.img.url}' width=50>")

    get_html_a_img.short_description = 'Фотография'
    get_html_img.short_description = 'Изображение на данный момент'


class HashtagsNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'hashtag', 'date_creation', 'date_changes')
    list_display_links = ('id', 'hashtag')
    search_fields = ('id',)


class HashtagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'hashtag', 'gallery', 'date_creation', 'date_changes')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_filter = ('hashtag', 'gallery')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_services', 'get_html_a_img_background_services', 'question_price', 'price', 'publication', 'description', 'date_creation', 'date_changes')
    list_display_links = ('id', 'name_services')
    search_fields = ('id',)
    list_editable = ('publication',)
    fields = ('name_services', ('img_background_services', 'get_html_img_background_services'), 'question_price', 'price', 'publication', 'description', 'date_creation', 'date_changes')
    readonly_fields = ('get_html_img_background_services', 'date_creation', 'date_changes')

    def get_html_a_img_background_services(self, object):
        if object.img_background_services:
            return mark_safe(f"<img src='{object.img_background_services.url}' width=50> <a href='{object.img_background_services.url}'>{object.img_background_services}</a>")

    def get_html_img_background_services(self, object):
        if object.img_background_services:
            return mark_safe(
                f"<img src='{object.img_background_services.url}' width=50>")

    get_html_a_img_background_services.short_description = 'Изображение на заднем фоне'
    get_html_img_background_services.short_description = 'Изображение на данный момент'


class SpecificsServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'services', 'specifics', 'date_creation', 'date_changes')
    list_display_links = ('id',)
    search_fields = ('services',)
    list_filter = ('services',)


class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_faq', 'description', 'publication', 'date_creation', 'date_changes')
    list_display_links = ('id', 'name_faq')
    search_fields = ('id',)
    list_editable = ('publication',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name_reviewer', 'review', 'get_html_a_img_reviewer', 'social_networks', 'publication', 'gallery', 'date_creation')
    list_display_links = ('name_reviewer', 'review')
    search_fields = ('gallery',)
    list_editable = ('publication',)
    fields = ('name_reviewer', 'review', ('img_reviewer', 'get_html_img_reviewer'), 'social_networks', 'publication', 'gallery', 'date_creation')
    readonly_fields = ('get_html_img_reviewer', 'date_creation', 'date_changes')

    def get_html_a_img_reviewer(self, object):
        if object.img_reviewer:
            return mark_safe(f"<img src='{object.img_reviewer.url}' width=50> <a href='{object.img_reviewer.url}'>{object.img_reviewer}</a>")

    def get_html_img_reviewer(self, object):
        if object.img_reviewer:
            return mark_safe(f"<img src='{object.img_reviewer.url}' width=50>")

    get_html_a_img_reviewer.short_description = 'Фотография клиента или альбома'
    get_html_img_reviewer.short_description = 'Изображение на данный момент'


class OrderServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'call', 'email', 'service', 'message', 'date_creation', 'date_changes')
    list_display_links = ('id', 'name')
    search_fields = ('id',)
    list_filter = ('service',)


class OrderCallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'call', 'message', 'date_creation', 'date_changes')
    list_display_links = ('id', 'name')
    search_fields = ('id',)


class EmailSendUsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_email', 'to_email', 'password', 'smtp_host')
    list_display_links = ('id', 'from_email',)
    search_fields = ('id',)


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Img, ImgAdmin)
admin.site.register(HashtagsName, HashtagsNameAdmin)
admin.site.register(Hashtags, HashtagsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(SpecificsServices, SpecificsServicesAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(OrderService, OrderServiceAdmin)
admin.site.register(OrderCall, OrderCallAdmin)
admin.site.register(EmailSendUsers, EmailSendUsersAdmin)


admin.site.site_title = 'Админ-панель сайта Данила Селиния'
admin.site.site_header = 'Админ-панель сайта Данила Селиния'