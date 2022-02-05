# Generated by Django 3.2.9 on 2021-11-13 12:52

import bookingApps.utils.photo_utils
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200)),
                ('rating', models.FloatField(max_length=3, validators=[django.core.validators.MinValueValidator(1, 3), django.core.validators.MaxValueValidator(5, 3)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comments_user',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='PhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to=bookingApps.utils.photo_utils.PhotoCommentUserUtils.upload_to)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_comments_user', to='comments_user.commentsusermodel')),
            ],
            options={
                'db_table': 'photo_comments_user',
            },
        ),
    ]