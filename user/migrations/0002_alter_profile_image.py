# Generated by Django 3.2 on 2021-04-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='download.jpg', upload_to='profile_picture'),
        ),
    ]
