# Generated by Django 3.2.2 on 2021-05-28 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='certificate_type',
        ),
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.RemoveField(
            model_name='student',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school',
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
