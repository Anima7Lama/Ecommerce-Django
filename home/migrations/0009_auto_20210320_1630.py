# Generated by Django 3.1.7 on 2021-03-20 10:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210314_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
