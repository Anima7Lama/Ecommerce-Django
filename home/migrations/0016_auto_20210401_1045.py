# Generated by Django 3.1.7 on 2021-04-01 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210329_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Total',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_fee',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.FloatField(null=True),
        ),
    ]
