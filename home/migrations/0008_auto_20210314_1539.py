# Generated by Django 3.1.7 on 2021-03-14 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210310_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.brand'),
        ),
    ]
