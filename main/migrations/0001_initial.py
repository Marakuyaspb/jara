# Generated by Django 5.1.1 on 2025-01-29 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id_brand', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(default='Audi', max_length=30, verbose_name='Марка')),
            ],
            options={
                'verbose_name': 'Марка',
                'verbose_name_plural': 'Марка',
                'ordering': ['brand'],
                'indexes': [models.Index(fields=['brand'], name='main_brand_brand_07e57d_idx')],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='ПОЛНОЕ название модели')),
                ('variant', models.CharField(blank=True, max_length=250, null=True, verbose_name='Модель')),
                ('seria', models.CharField(blank=True, max_length=250, null=True, verbose_name='Серия')),
                ('power_cold', models.CharField(blank=True, max_length=250, null=True, verbose_name='Охлаждение, Вт')),
                ('power_hot', models.CharField(blank=True, max_length=250, null=True, verbose_name='Нагрев, Вт')),
                ('square', models.CharField(blank=True, max_length=250, null=True, verbose_name='Площадь, м²')),
                ('t_cold', models.CharField(blank=True, max_length=250, null=True, verbose_name='Охлаждение (С°)')),
                ('t_hot', models.CharField(blank=True, max_length=250, null=True, verbose_name='Нагрев (С°)')),
                ('features', models.CharField(blank=True, max_length=250, null=True, verbose_name='Особенности')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Цена')),
                ('img_1', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Фото 1')),
                ('img_2', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Фото 2')),
                ('img_3', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Фото 3')),
                ('img_4', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Фото 4')),
                ('img_5', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Фото 5')),
                ('img_6', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Фото 6')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='main.brand', verbose_name='Марка')),
            ],
        ),
    ]
