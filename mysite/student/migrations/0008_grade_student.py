# Generated by Django 3.2.2 on 2021-05-28 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20210528_0754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('certificate_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.certificate_type')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.department')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.grade')),
                ('school', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='student.school')),
            ],
        ),
    ]
