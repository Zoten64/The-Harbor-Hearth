# Generated by Django 5.0.4 on 2024-05-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='home_page',
            field=models.BooleanField(default=False),
        ),
    ]
