# Generated by Django 4.0.5 on 2022-07-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_tag_alter_post_category_alter_post_slug_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slider_post',
            field=models.BooleanField(default=False),
        ),
    ]
