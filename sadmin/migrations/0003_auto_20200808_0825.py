# Generated by Django 3.0.8 on 2020-08-08 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0002_surveyor_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyor',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
