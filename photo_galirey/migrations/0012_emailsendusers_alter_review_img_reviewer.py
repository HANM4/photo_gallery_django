# Generated by Django 4.1.5 on 2023-04-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_galirey', '0011_alter_faq_options_alter_gallery_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSendUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.EmailField(max_length=254, verbose_name='Электронная почта отправки')),
                ('to_email', models.EmailField(max_length=254, verbose_name='Электронная почта приема')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль для почты отправки')),
                ('smtp_host', models.EmailField(max_length=254, verbose_name='SMTP хост')),
            ],
            options={
                'verbose_name': 'Данные email почты для отправки',
                'verbose_name_plural': 'Данные email почт для отправки',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='review',
            name='img_reviewer',
            field=models.ImageField(upload_to='', verbose_name='Фотография клиента или альбома'),
        ),
    ]
