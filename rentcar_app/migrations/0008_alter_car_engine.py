# Generated by Django 4.0.3 on 2022-04-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentcar_app', '0007_alter_rent_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
    ]
