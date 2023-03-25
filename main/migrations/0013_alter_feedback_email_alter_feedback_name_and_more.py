# Generated by Django 4.1.7 on 2023-03-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_redirect_is_root_redirect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Сообщение'),
        ),
    ]
