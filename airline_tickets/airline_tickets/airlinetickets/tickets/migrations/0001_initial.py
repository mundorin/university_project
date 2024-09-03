# Generated by Django 5.0 on 2023-12-18 18:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flyes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival', models.CharField(max_length=255)),
                ('departure', models.CharField(max_length=255)),
                ('departure_date', models.DateTimeField()),
                ('arrival_date', models.DateTimeField()),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Таблица рейсов',
                'verbose_name_plural': 'Таблица рейсов',
                'ordering': ['arrival'],
            },
        ),
        migrations.CreateModel(
            name='SoldTickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_number', models.IntegerField()),
                ('flyes_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tickets.flyes')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('bought_tickets', models.ManyToManyField(to='tickets.soldtickets')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
            },
        ),
    ]
