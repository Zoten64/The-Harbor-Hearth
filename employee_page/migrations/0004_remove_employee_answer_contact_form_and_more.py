# Generated by Django 5.0.4 on 2024-05-24 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_page', '0003_employeecontactanswer_employee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='answer_contact_form',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='view_orders',
        ),
    ]