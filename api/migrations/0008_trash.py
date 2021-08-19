# Generated by Django 2.2.12 on 2021-08-19 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_delete_trash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=15)),
                ('type_probability', models.IntegerField(default=0)),
                ('foreign_subst', models.CharField(max_length=50)),
                ('foreign_subst_probability', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('feedback_type', models.CharField(max_length=15)),
                ('feedback_foreign_subst', models.BooleanField()),
            ],
        ),
    ]