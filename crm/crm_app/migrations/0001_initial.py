# Generated by Django 4.2.16 on 2024-10-25 03:27

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('position', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('notes', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('lead', 'Lead'), ('customer', 'Customer'), ('inactive', 'Inactive')], default='lead', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
