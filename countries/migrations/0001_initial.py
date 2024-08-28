# Generated by Django 5.1 on 2024-08-27 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('attr_id', models.AutoField(primary_key=True, serialize=False)),
                ('attr_name', models.CharField(max_length=200)),
                ('attr_description', models.TextField()),
                ('attr_category_id', models.IntegerField()),
                ('attr_image_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('loc_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image_url', models.URLField(blank=True, null=True)),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='countries.country')),
            ],
        ),
    ]
