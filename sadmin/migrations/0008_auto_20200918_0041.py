# Generated by Django 3.0.8 on 2020-09-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0007_auto_20200911_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_author',
            field=models.CharField(max_length=200),
        ),
    ]
