# Generated by Django 3.2.9 on 2021-12-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments_apartment', '0006_auto_20211208_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsapartmentmodel',
            name='name_user',
            field=models.CharField(default='Anonymous', max_length=30),
        ),
    ]