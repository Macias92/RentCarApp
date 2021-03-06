# Generated by Django 4.0.3 on 2022-03-21 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(0, 'Audi'), (1, 'BMW'), (2, 'Citroen'), (3, 'Fiat'), (4, 'Ford'), (5, 'Hyundai'), (6, 'Kia'), (7, 'Lexus'), (8, 'Mazda'), (9, 'Mercedes'), (10, 'Nissan'), (11, 'Opel'), (12, 'Renault'), (13, 'SEAT'), (14, 'Skoda'), (15, 'Tesla'), (16, 'Toyota'), (17, 'Volkswagen'), (18, 'Volvo')])),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('power', models.IntegerField()),
                ('engine', models.DecimalField(decimal_places=1, max_digits=2)),
                ('year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('seats', models.IntegerField()),
                ('gears', models.IntegerField(choices=[(0, 'automatic'), (1, 'manual')])),
                ('fuel', models.IntegerField(choices=[(0, 'petrol'), (1, 'oil'), (2, 'petrol+LPG'), (3, 'hybrid'), (4, 'electric')])),
                ('price_per_day', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentcar_app.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(0, 'Convertible'), (1, 'Coupe'), (2, 'Hatchback'), (3, 'Minivan'), (4, 'Pickup Truck'), (5, 'Sedan'), (6, 'Sports Car'), (7, 'Station Wagon'), (8, 'SUV')])),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentcar_app.car')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rentcar_app.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel_num', models.IntegerField()),
                ('address', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=64)),
                ('zip_code', models.CharField(blank=True, max_length=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentcar_app.type'),
        ),
    ]
