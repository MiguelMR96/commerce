# Generated by Django 4.0 on 2023-05-25 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=48),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]