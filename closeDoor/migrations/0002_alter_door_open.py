# Generated by Django 3.2.6 on 2021-08-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closeDoor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='open',
            field=models.CharField(max_length=300),
        ),
    ]
