# Generated by Django 4.1.5 on 2023-03-18 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo_galirey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_services', models.CharField(help_text='Не больше 255 символов', max_length=255, null=True)),
                ('img_background_services', models.ImageField(upload_to='')),
                ('question_price', models.CharField(help_text='Не больше 255 символов', max_length=255, null=True)),
                ('price', models.IntegerField(help_text='Не больше 255 цифр', max_length=255, null=True)),
                ('description', models.CharField(help_text='Не больше 255 символов', max_length=255, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_changes', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecificsServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifics', models.CharField(help_text='Не больше 255 символов', max_length=255, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_changes', models.DateTimeField(auto_now=True)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo_galirey.gallery')),
            ],
        ),
    ]
