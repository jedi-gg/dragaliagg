# Generated by Django 3.2.8 on 2021-11-15 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comps', '0017_alter_compquest_image_offset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comp',
            name='game_version',
        ),
    ]
