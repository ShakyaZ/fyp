# Generated by Django 4.0.1 on 2022-01-15 09:12

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
            name='Vet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('contact', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('isactive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_status', models.BooleanField(default=True)),
                ('payment_status', models.BooleanField(default=True)),
                ('appointment_created_date', models.DateTimeField()),
                ('appointment_date', models.DateTimeField()),
                ('cancel', models.BooleanField()),
                ('cancel_reason', models.CharField(max_length=250)),
                ('fees', models.CharField(max_length=250)),
                ('user_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vet_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.vet')),
            ],
        ),
    ]
