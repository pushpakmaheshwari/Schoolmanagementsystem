# Generated by Django 3.0.5 on 2020-07-23 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EDApp', '0016_employee_name_of_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='name_of_class',
        ),
    ]