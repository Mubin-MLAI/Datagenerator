# Generated by Django 5.0.6 on 2024-06-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datageneratorapp', '0005_alter_allscenario_entry_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allscenario',
            old_name='specific_ppt',
            new_name='basic_sa',
        ),
        migrations.AddField(
            model_name='allscenario',
            name='maturity_age',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='allscenario',
            name='policy_term',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='allscenario',
            name='premium',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
