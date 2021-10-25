# Generated by Django 3.2.8 on 2021-10-25 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comps', '0002_compquest_banner_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='', editable=False, max_length=120)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
