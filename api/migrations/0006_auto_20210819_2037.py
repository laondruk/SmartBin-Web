# Generated by Django 2.2.12 on 2021-08-19 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210819_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trash',
            name='foreign_subst_probability',
            field=models.CharField(max_length=500),
        ),
    ]