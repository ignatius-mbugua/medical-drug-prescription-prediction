# Generated by Django 2.1.7 on 2019-04-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0010_auto_20190422_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientdetail',
            old_name='weight',
            new_name='weight_in_kg',
        ),
        migrations.RemoveField(
            model_name='patientdetail',
            name='blood_pressure',
        ),
        migrations.RemoveField(
            model_name='patientdetail',
            name='height',
        ),
        migrations.RemoveField(
            model_name='patientdetail',
            name='potassium',
        ),
        migrations.RemoveField(
            model_name='patientdetail',
            name='sodium',
        ),
        migrations.AddField(
            model_name='patientdetail',
            name='alcoholic',
            field=models.CharField(blank=True, choices=[('Y', 'yes'), ('N', 'no')], max_length=1),
        ),
        migrations.AddField(
            model_name='patientdetail',
            name='breast_feeding',
            field=models.CharField(blank=True, choices=[('Y', 'yes'), ('N', 'no')], max_length=1),
        ),
        migrations.AddField(
            model_name='patientdetail',
            name='diabetes',
            field=models.CharField(blank=True, choices=[('Y', 'yes'), ('N', 'no')], max_length=1),
        ),
        migrations.AddField(
            model_name='patientdetail',
            name='eye_disease',
            field=models.CharField(blank=True, choices=[('Y', 'yes'), ('N', 'no')], max_length=1),
        ),
        migrations.AddField(
            model_name='patientdetail',
            name='kidney_disease',
            field=models.CharField(blank=True, choices=[('Y', 'yes'), ('N', 'no')], max_length=1),
        ),
        migrations.AddField(
            model_name='patientdetail',
            name='liver_disease',
            field=models.CharField(blank=True, choices=[('Y', 'yes'), ('N', 'no')], max_length=1),
        ),
        migrations.AddField(
            model_name='patientdetail',
            name='pregnant',
            field=models.CharField(blank=True, choices=[('Y', 'yes'), ('N', 'no')], max_length=1),
        ),
        migrations.AlterField(
            model_name='patientdetail',
            name='disease_identified',
            field=models.CharField(blank=True, choices=[('Y', 'yes'), ('N', 'no')], max_length=1),
        ),
        migrations.AlterField(
            model_name='patientdetail',
            name='medicine',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]