# Generated by Django 3.0.5 on 2020-07-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDApp', '0007_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=10)),
                ('description', models.CharField(max_length=300)),
                ('income', models.FloatField()),
                ('expense', models.FloatField()),
            ],
        ),
    ]
