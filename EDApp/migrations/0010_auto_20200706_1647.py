# Generated by Django 3.0.5 on 2020-07-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDApp', '0009_auto_20200706_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='expense',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='income',
            field=models.FloatField(default=0),
        ),
    ]
