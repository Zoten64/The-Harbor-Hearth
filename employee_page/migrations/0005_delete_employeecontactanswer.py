# Generated by Django 5.0.4 on 2024-05-24 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_page', '0004_remove_employee_answer_contact_form_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmployeeContactAnswer',
        ),
    ]
