# Generated by Django 3.2.9 on 2022-01-15 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments_apartment', '0008_auto_20220108_1216'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PhotoModel',
            new_name='PhotoModelCommentsApartment',
        ),
    ]