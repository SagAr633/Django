# Generated by Django 4.0.3 on 2022-05-11 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0013_remove_blogs_image_blogs_blog_image_alter_blogs_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]
