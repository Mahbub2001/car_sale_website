# Generated by Django 5.0.4 on 2024-05-07 10:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars_brand', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars_brand.brand')),
                ('description', models.CharField(max_length=255)),
                ('buyers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
