# Generated by Django 4.1.5 on 2023-04-02 12:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_galirey', '0009_faq_publication_gallery_publication_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call', models.CharField(max_length=18, validators=[django.core.validators.RegexValidator(regex='\\+7 \\(\\d{3}\\) \\d{3}-\\d{2}-\\d{2}')])),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
