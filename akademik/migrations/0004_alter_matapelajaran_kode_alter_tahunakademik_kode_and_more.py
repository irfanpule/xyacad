# Generated by Django 4.0.6 on 2023-08-07 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0003_rename_khusu_matapelajaran_khusus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matapelajaran',
            name='kode',
            field=models.CharField(max_length=150, unique=True, verbose_name='Kode Mata Pelajaran'),
        ),
        migrations.AlterField(
            model_name='tahunakademik',
            name='kode',
            field=models.CharField(max_length=150, unique=True, verbose_name='Kode Tahun Akademik'),
        ),
        migrations.AlterField(
            model_name='tingkat',
            name='kode',
            field=models.CharField(max_length=150, unique=True, verbose_name='Kode Tingkat'),
        ),
    ]
