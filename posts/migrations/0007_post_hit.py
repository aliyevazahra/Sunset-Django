# Generated by Django 4.0.5 on 2022-07-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_slider_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
