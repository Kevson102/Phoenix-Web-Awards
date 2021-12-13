# Generated by Django 3.2.9 on 2021-12-13 05:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webawards', '0006_votes_avg_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='Avg_score',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
