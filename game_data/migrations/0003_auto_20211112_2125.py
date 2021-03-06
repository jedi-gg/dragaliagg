# Generated by Django 3.2.8 on 2021-11-12 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_data', '0002_wyrmprint_image_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventurer',
            name='shared_skill_cost',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adventurer',
            name='shared_skill_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adventurer',
            name='shared_skill_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='adventurer',
            name='shared_skill_sp',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
