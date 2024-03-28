# Generated by Django 4.1.2 on 2024-03-21 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RuralPopulationApp', '0004_remove_country_value_remove_country_years_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomecountries',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RuralPopulationApp.country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regioncountries',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RuralPopulationApp.country'),
            preserve_default=False,
        ),
    ]
