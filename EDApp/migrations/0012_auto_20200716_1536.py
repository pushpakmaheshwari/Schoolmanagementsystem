# Generated by Django 3.0.5 on 2020-07-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDApp', '0011_employee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='adminssion_date',
            field=models.DateField(max_length=10),
        ),
    ]
