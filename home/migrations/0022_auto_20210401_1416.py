# Generated by Django 3.1.7 on 2021-04-01 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210401_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
