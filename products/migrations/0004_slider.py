# Generated by Django 4.0.2 on 2022-02-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_basket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='slider_images')),
                ('css', models.CharField(default='-', max_length=200, null=True, verbose_name='CSS Класс')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
