# Generated by Django 4.1 on 2022-10-14 20:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlogs', '0009_remove_busquedafiltrada_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busquedafiltrada',
            name='nombre_autor',
            field=ckeditor.fields.RichTextField(max_length=400),
        ),
    ]
