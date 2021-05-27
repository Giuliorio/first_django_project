# Generated by Django 3.2.2 on 2021-05-27 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210527_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='student.school'),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.faculty')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.grade'),
        ),
    ]