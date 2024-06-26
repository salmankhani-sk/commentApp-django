# Generated by Django 5.0.6 on 2024-06-08 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subjectcode', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacherId', models.IntegerField(primary_key=True, serialize=False)),
                ('qualification', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('subjectCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.subject')),
            ],
        ),
    ]
