# Generated by Django 4.0.3 on 2022-03-23 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentcar_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='name',
            new_name='model',
        ),
    ]
