# Generated by Django 3.2.8 on 2021-10-25 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comps', '0004_comp_comp_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comp',
            name='clear_rate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comp',
            name='clear_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]