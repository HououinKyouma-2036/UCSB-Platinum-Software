# Generated by Django 4.2.9 on 2024-02-14 06:58

import django.core.validators
from django.db import migrations, models
import search.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cached_Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseID', models.CharField(max_length=30)),
                ('quarter', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('year', models.IntegerField(validators=[search.validators.validate_four_digit_number])),
                ('data', models.JSONField()),
            ],
            options={
                'unique_together': {('courseID', 'quarter', 'year')},
            },
        ),
    ]
