# Generated by Django 3.2.6 on 2021-08-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_trash_type_probability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trash',
            name='image',
            field=models.BinaryField(),
        ),
    ]
