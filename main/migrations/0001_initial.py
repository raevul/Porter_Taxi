# Generated by Django 5.0.3 on 2024-03-16 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('weight', models.CharField(default='...', max_length=40)),
                ('image', models.ImageField(upload_to='services', verbose_name='Картинка')),
            ],
        ),
    ]
