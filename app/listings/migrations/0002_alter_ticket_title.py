# Generated by Django 4.1.3 on 2022-11-10 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
