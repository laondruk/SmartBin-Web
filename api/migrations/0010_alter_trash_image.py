# Generated by Django 3.2.6 on 2021-08-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210819_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trash',
            name='image',
            field=models.ImageField(upload_to='TrashImages'),
        ),
    ]
