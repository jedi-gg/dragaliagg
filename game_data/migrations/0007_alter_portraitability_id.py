# Generated by Django 3.2.8 on 2022-01-02 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_data', '0006_alter_portraitability_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portraitability',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]