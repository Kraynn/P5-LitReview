# Generated by Django 4.1.3 on 2022-11-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_ticket_description_ticket_image_ticket_time_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(default='', upload_to='img'),
            preserve_default=False,
        ),
    ]
