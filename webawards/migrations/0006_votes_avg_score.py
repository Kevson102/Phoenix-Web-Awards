# Generated by Django 3.2.9 on 2021-12-13 05:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webawards', '0005_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='votes',
            name='Avg_score',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
