# Generated by Django 5.0.4 on 2024-04-19 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(0, 'Meal'), (1, 'Drink'), (2, 'Dessert')], default=0)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('ingridients', models.TextField()),
                ('price', models.IntegerField()),
                ('vegan', models.BooleanField(default=False)),
                ('nuts', models.BooleanField(default=False)),
                ('lactose', models.BooleanField(default=False)),
                ('gluten', models.BooleanField(default=False)),
                ('eggs', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['category'],
            },
        ),
    ]