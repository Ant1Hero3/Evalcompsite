# Generated by Django 3.1.3 on 2020-11-24 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evalcompsite', '0003_auto_20201125_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.CharField(max_length=255, verbose_name='Электронный адрес'),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone_number',
            field=models.CharField(max_length=255, verbose_name='Номер телефона'),
        ),
    ]
