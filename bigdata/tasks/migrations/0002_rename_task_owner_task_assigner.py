# Generated by Django 4.0 on 2022-07-20 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_owner',
            new_name='assigner',
        ),
    ]