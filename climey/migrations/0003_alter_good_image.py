# Generated by Django 3.2.13 on 2022-06-19 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climey', '0002_alter_good_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(upload_to='climey/image/'),
        ),
    ]