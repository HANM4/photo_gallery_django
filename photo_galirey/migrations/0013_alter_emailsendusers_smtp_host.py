# Generated by Django 4.1.5 on 2023-04-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_galirey', '0012_emailsendusers_alter_review_img_reviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsendusers',
            name='smtp_host',
            field=models.CharField(max_length=50, verbose_name='SMTP хост'),
        ),
    ]
