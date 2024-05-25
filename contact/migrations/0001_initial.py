# Generated by Django 5.0.4 on 2024-05-25 21:16

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
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('preferred_contact', models.CharField(choices=[('PHONE', 'phone'), ('EMAIL', 'E-mail')])),
                ('message', models.CharField(max_length=1500)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('answered', models.BooleanField(default=False)),
                ('employee_response', models.CharField(max_length=1500, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_employee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
