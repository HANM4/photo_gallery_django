# Generated by Django 4.1.5 on 2023-04-02 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_galirey', '0008_orderservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='publication',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gallery',
            name='publication',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='publication',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='services',
            name='publication',
            field=models.BooleanField(default=False),
        ),
    ]
