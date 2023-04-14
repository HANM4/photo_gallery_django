from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class Gallery(models.Model):
    name_work = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True, verbose_name='Название альбома')
    img_background_work = models.ImageField(verbose_name='Обложка альбома')
    publication = models.BooleanField(default=False, verbose_name='Опубликовано')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    date_changes = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.name_work

    def get_absolute_url(self):
        return reverse('gallery_int', kwargs={'gallery_id': self.pk})

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['id']


class Img(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='Альбом')
    img = models.ImageField(verbose_name='Фотография')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    date_changes = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        verbose_name = 'Фотография в альбомах'
        verbose_name_plural = 'Фотографии в альбомах'
        ordering = ['gallery']


class HashtagsName(models.Model):
    hashtag = models.CharField(max_length=50, help_text='Не больше 50 символов', null=True, verbose_name='Название категории')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    date_changes = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.hashtag

    def get_absolute_url(self):
        return reverse('hashtag', kwargs={'hashtags_id': self.pk})

    class Meta:
        verbose_name = 'Существующая категория'
        verbose_name_plural = 'Существующие категории'
        ordering = ['id']


class Hashtags(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='Альбом')
    hashtag = models.ForeignKey(HashtagsName, on_delete=models.CASCADE, verbose_name='Категория')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    date_changes = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        verbose_name = 'Альбомы и их категории'
        verbose_name_plural = 'Альбомы и их категории'
        ordering = ['id']


class Services(models.Model):
    name_services = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True, verbose_name='Название услуги')
    img_background_services = models.ImageField(verbose_name='Изображение на заднем фоне')
    question_price = models.TextField(max_length=255, help_text='Не больше 255 символов', null=True, verbose_name='Обоснование цены')
    price = models.IntegerField(help_text='Не больше 255 цифр', null=True, verbose_name='Цена руб.')
    publication = models.BooleanField(default=False, verbose_name='Опубликовано')
    description = models.TextField(max_length=255, help_text='Не больше 255 символов', null=True, verbose_name='Описание услуги')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    date_changes = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.name_services

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['id']


class SpecificsServices(models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуга')
    specifics = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True, verbose_name='Основной пункт')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    date_changes = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.specifics

    class Meta:
        verbose_name = 'Основные пункты услуги'
        verbose_name_plural = 'Основные пункты услуги'
        ordering = ['services']


class FAQ(models.Model):
    name_faq = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True, verbose_name='Вопрос')
    description = models.TextField(max_length=1000, help_text='Не больше 1000 символов', null=True, verbose_name='Ответ')
    publication = models.BooleanField(default=False, verbose_name='Опубликовано')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    date_changes = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.name_faq

    class Meta:
        verbose_name = 'Часто задаваемые вопросы'
        verbose_name_plural = 'Часто задаваемые вопросы'
        ordering = ['id']


class Review(models.Model):
    name_reviewer = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True, verbose_name='ФИО клиента')
    review = models.TextField(max_length=1000, help_text='Не больше 1000 символов', null=True, verbose_name='Текст отзыва')
    img_reviewer = models.ImageField(verbose_name='Фотография клиента или альбома')
    social_networks = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True, verbose_name='Социальные сети клиента')
    publication = models.BooleanField(default=False, verbose_name='Опубликовано')
    gallery = models.OneToOneField(Gallery, on_delete=models.CASCADE, primary_key=True)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    date_changes = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def save(self, *args, **kwargs):
        if not self.img_reviewer:
            self.img_reviewer = self.gallery.img_background_work
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_reviewer

    def get_absolute_url(self):
        return reverse('review_int', kwargs={'review_id': self.pk})

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['gallery']


class OrderService(models.Model):
    phone_number_regex = RegexValidator(regex=r"\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}")
    call = models.CharField(validators=[phone_number_regex], max_length=18, verbose_name='Номер телефона клиента')
    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Заказанная услуга')
    name = models.CharField(max_length=50, verbose_name='ФИО клиента')
    email = models.EmailField(verbose_name='Электронная почта клиента')
    message = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Комментарий к заказу')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    date_changes = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказанные услуги'
        verbose_name_plural = 'Заказанные услуги'
        ordering = ['service']


class OrderCall(models.Model):
    phone_number_regex = RegexValidator(regex=r"\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}")
    call = models.CharField(validators=[phone_number_regex], max_length=18, verbose_name='Номер телефона клиента')
    name = models.CharField(max_length=50, verbose_name='ФИО клиента')
    message = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Комментарий к заказу')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    date_changes = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказанные звонки'
        verbose_name_plural = 'Заказанные звонки'
        ordering = ['id']