# Generated by Django 2.0.6 on 2018-07-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20180705_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, upload_to='notes/'),
        ),
    ]
