# Generated by Django 4.1.7 on 2023-03-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_page_content_alter_pageblock_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='cropped_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/cropped/'),
        ),
    ]
