# Generated by Django 3.2.24 on 2024-02-09 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('time_minutes', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('link', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]