# Generated by Django 3.0.5 on 2020-07-23 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EDApp', '0014_auto_20200723_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='name_of_class',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='EDApp.EdsysClass'),
        ),
    ]
