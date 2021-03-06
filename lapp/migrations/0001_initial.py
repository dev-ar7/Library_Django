# Generated by Django 3.2.8 on 2021-10-27 15:23

from django.db import migrations, models
import django.db.models.deletion
import lapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200)),
                ('book_author', models.CharField(max_length=150)),
                ('book_pages', models.IntegerField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.CharField(max_length=25)),
                ('std_name', models.CharField(max_length=250)),
                ('std_address', models.CharField(max_length=500)),
                ('std_batch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IssueBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(auto_now=True)),
                ('return_date', models.DateTimeField(default=lapp.models.returned_date)),
                ('score', models.CharField(default='Some Scores', max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lapp.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lapp.students')),
            ],
        ),
    ]
