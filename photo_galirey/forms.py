from django import forms
from .models import *
from django.core.validators import RegexValidator


class OrderCallForm(forms.ModelForm):
    class Meta:
        model = OrderCall
        fields = '__all__'


class OrderServiceForm(forms.ModelForm):
    class Meta:
        model = OrderService
        fields = ['call', 'service', 'name', 'email', 'message']


class WriteReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name_reviewer', 'review', 'social_networks', 'gallery']
