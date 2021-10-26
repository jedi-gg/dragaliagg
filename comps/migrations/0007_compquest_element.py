# Generated by Django 3.2.8 on 2021-10-26 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comps', '0006_auto_20211025_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='compquest',
            name='element',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'WIND'), (2, 'WATER'), (3, 'FLAME'), (4, 'LIGHT'), (5, 'SHADOW')], null=True),
        ),
    ]