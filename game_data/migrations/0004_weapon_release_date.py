# Generated by Django 3.2.8 on 2021-12-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_data', '0003_auto_20211112_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]