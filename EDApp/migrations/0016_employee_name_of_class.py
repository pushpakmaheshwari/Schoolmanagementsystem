# Generated by Django 3.0.5 on 2020-07-23 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EDApp', '0015_students_name_of_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='name_of_class',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='EDApp.EdsysClass'),
        ),
    ]
