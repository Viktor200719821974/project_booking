# Generated by Django 3.2.9 on 2021-11-11 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apartments', '0002_apartmentmodel_user_apartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentmodel',
            name='user_apartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment', to=settings.AUTH_USER_MODEL),
        ),
    ]
