# Generated by Django 5.0.4 on 2024-05-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Finished', 'Finished'), ('Cancelled', 'Cancelled')], default=0),
        ),
    ]
