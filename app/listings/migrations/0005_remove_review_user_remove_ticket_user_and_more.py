# Generated by Django 4.1.3 on 2022-11-15 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_ticket_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserFollows',
        ),
    ]
