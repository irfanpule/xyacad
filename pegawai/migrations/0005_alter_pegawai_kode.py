# Generated by Django 4.0.6 on 2023-08-07 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegawai', '0004_alter_golongan_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegawai',
            name='kode',
            field=models.CharField(max_length=100, unique=True, verbose_name='Kode Pegawai'),
        ),
    ]