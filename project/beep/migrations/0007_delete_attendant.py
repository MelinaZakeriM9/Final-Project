# Generated by Django 5.0.6 on 2024-06-29 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beep', '0006_alter_event_creator'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendant',
        ),
    ]