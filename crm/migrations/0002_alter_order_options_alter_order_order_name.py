# Generated by Django 4.0.5 on 2022-06-04 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterField(
            model_name='order',
            name='order_name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
