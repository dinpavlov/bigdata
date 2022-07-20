# Generated by Django 4.0 on 2022-07-20 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(blank=True, max_length=100, verbose_name='название задачи')),
                ('task_endtime', models.DateTimeField()),
                ('task_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='auth.user')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]