# Generated by Django 2.1.4 on 2018-12-16 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20181216_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='profile_pic/avatar.png', upload_to='profile_pic/photos/%Y/%m/%d/'),
        ),
    ]
