# Generated by Django 4.0.6 on 2023-12-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegawai', '0006_presensi'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='presensi',
            options={'verbose_name': 'Presensi', 'verbose_name_plural': 'Presensi'},
        ),
        migrations.AlterField(
            model_name='presensi',
            name='ket',
            field=models.TextField(blank=True, default='', help_text='Keterangan atau link ref dokumen', null=True, verbose_name='Keterangan'),
        ),
    ]
