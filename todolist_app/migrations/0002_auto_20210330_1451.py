# Generated by Django 2.2.10 on 2021-03-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskslist',
            name='email',
            field=models.EmailField(default='<django.db.models.fields.CharField>@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='taskslist',
            name='name',
            field=models.CharField(default='new_user', max_length=100),
        ),
    ]
