# Generated by Django 2.2.6 on 2020-08-06 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0013_auto_20200614_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_img',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Изображение книги'),
        ),
    ]