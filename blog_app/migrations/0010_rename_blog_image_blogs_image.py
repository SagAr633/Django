# Generated by Django 4.0.3 on 2022-05-11 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_alter_blogs_blog_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='blog_image',
            new_name='image',
        ),
    ]
