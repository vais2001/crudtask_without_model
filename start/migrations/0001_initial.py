# Generated by Django 4.2.4 on 2023-08-22 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('worker_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]