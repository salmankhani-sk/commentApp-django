# Generated by Django 5.0.6 on 2024-06-08 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_usercomments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subjectCode',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
