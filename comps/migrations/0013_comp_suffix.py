# Generated by Django 3.2.8 on 2021-11-04 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comps', '0012_alter_compquest_is_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='comp',
            name='suffix',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
