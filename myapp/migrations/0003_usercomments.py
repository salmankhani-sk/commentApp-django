# Generated by Django 5.0.6 on 2024-06-08 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_subject_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
    ]
