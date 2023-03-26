from django.db import models
from django.urls import reverse


class Gallery(models.Model):
    name_work = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True)
    img_background_work = models.ImageField()
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
    date_creation = models.DateTimeField(auto_now_add=True)
    date_changes = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_faq


class Review(models.Model):
    name_reviewer = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True)
    review = models.TextField(max_length=1000, help_text='Не больше 1000 символов', null=True)
    img_reviewer = models.ImageField()
    social_networks = models.CharField(max_length=255, help_text='Не больше 255 символов', null=True)
    gallery = models.OneToOneField(Gallery, on_delete=models.CASCADE, primary_key=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_changes = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_reviewer

    def get_absolute_url(self):
        return reverse('review_int', kwargs={'review_id': self.pk})
