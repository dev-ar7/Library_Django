# Generated by Django 3.2.8 on 2021-10-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_pages',
            field=models.IntegerField(),
        ),
    ]
