# Generated by Django 3.2.9 on 2022-01-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('date_selection', '0002_auto_20220110_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='dateselectionmodel',
            name='surname_user',
            field=models.CharField(default='Anonymous', max_length=20),
        ),
    ]