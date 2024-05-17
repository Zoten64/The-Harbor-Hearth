# Generated by Django 5.0.4 on 2024-05-12 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_delivery_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='finished',
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('Not Started', 'NOT-STARTED'), ('In progress', 'IN-PROGRESS'), ('Finished', 'FINISHED')], default=0),
        ),
    ]