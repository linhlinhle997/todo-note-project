# Generated by Django 4.0.3 on 2022-04-22 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-created_date', '-is_done']},
        ),
    ]
