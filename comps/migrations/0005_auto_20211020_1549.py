# Generated by Django 3.2.8 on 2021-10-20 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comps', '0004_adventurerbuild'),
    ]

    operations = [
        migrations.AddField(
            model_name='comp',
            name='adventurer_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comp_adventurer_1', to='comps.adventurerbuild'),
        ),
        migrations.AddField(
            model_name='comp',
            name='adventurer_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comp_adventurer_2', to='comps.adventurerbuild'),
        ),
        migrations.AddField(
            model_name='comp',
            name='adventurer_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comp_adventurer_3', to='comps.adventurerbuild'),
        ),
        migrations.AddField(
            model_name='comp',
            name='adventurer_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comp_adventurer_4', to='comps.adventurerbuild'),
        ),
    ]
