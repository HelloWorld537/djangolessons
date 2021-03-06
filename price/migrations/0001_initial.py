# Generated by Django 4.0.5 on 2022-06-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_value', models.CharField(max_length=50, verbose_name='Price')),
                ('pc_desc', models.CharField(max_length=50, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Price Card',
                'verbose_name_plural': 'Prices Cards',
            },
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_title', models.CharField(max_length=50, verbose_name='Price Title')),
                ('pc_old_price', models.CharField(max_length=50, verbose_name='Old Price')),
                ('pc_new_price', models.CharField(max_length=50, verbose_name='New Price')),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
