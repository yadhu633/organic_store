# Generated by Django 4.2.7 on 2024-01-21 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_regshop_profaile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regshop',
            old_name='profaile',
            new_name='profile',
        ),
    ]