# Generated by Django 5.0.1 on 2024-03-26 07:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=500)),
                ('movie_poster', models.URLField(blank=True, null=True)),
                ('movie_name', models.CharField(max_length=500)),
                ('release_date', models.DateField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('review', models.TextField()),
            ],
        ),
    ]
