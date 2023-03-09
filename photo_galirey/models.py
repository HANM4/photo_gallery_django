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


class Hashtags(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(HashtagsName, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_changes = models.DateTimeField(auto_now=True)
