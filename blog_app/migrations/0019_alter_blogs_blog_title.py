# Generated by Django 4.0.3 on 2022-05-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0018_alter_blogs_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_title',
            field=models.TextField(max_length=250),
        ),
    ]
