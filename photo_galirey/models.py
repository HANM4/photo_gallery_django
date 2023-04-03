from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class Gallery(models.Model):
    name_work = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True)
    img_background_work = models.ImageField()
    publication = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_changes = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_work

    def get_absolute_url(self):
        return reverse('gallery_int', kwargs={'gallery_id': self.pk})


class Img(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    img = models.ImageField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_changes = models.DateTimeField(auto_now=True)


class HashtagsName(models.Model):
    hashtag = models.CharField(max_length=50, help_text='Не больше 50 символов', null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_changes = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hashtag

    def get_absolute_url(self):
        return reverse('hashtag', kwargs={'hashtags_id': self.pk})


class Hashtags(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(HashtagsName, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_changes = models.DateTimeField(auto_now=True)


class Services(models.Model):
    name_services = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True)
    img_background_services = models.ImageField()
    question_price = models.TextField(max_length=255, help_text='Не больше 255 символов', null=True)
    price = models.IntegerField(help_text='Не больше 255 цифр', null=True)
    publication = models.BooleanField(default=False)
    description = models.TextField(max_length=255, help_text='Не больше 255 символов', null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_changes = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_services


class SpecificsServices(models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    specifics = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_changes = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.specifics


class FAQ(models.Model):
    name_faq = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True)
    description = models.TextField(max_length=1000, help_text='Не больше 1000 символов', null=True)
    publication = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_changes = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_faq


class Review(models.Model):
    name_reviewer = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True)
    review = models.TextField(max_length=1000, help_text='Не больше 1000 символов', null=True)
    img_reviewer = models.ImageField()
    social_networks = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True)
    publication = models.BooleanField(default=False)
    gallery = models.OneToOneField(Gallery, on_delete=models.CASCADE, primary_key=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_changes = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.img_reviewer:
            self.img_reviewer = self.gallery.img_background_work
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_reviewer

    def get_absolute_url(self):
        return reverse('review_int', kwargs={'review_id': self.pk})


class OrderService(models.Model):
    phone_number_regex = RegexValidator(regex=r"\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}")
    call = models.CharField(validators=[phone_number_regex], max_length=18)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class OrderCall(models.Model):
    phone_number_regex = RegexValidator(regex=r"\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}")
    call = models.CharField(validators=[phone_number_regex], max_length=18)
    name = models.CharField(max_length=50)
    message = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name
