# Generated by Django 5.0.4 on 2024-05-25 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_alter_review_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]