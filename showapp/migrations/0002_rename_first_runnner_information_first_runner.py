# Generated by Django 4.0.5 on 2022-06-25 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='first_runnner',
            new_name='first_runner',
        ),
    ]
