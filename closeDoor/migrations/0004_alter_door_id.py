# Generated by Django 3.2.6 on 2021-08-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closeDoor', '0003_auto_20210807_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
