# Generated by Django 4.0.6 on 2023-08-07 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0006_alter_gedung_options_alter_jurusan_options_and_more'),
        ('akademik', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matapelajaran',
            name='guru',
        ),
        migrations.RemoveField(
            model_name='matapelajaran',
            name='jml_jam',
        ),
        migrations.AddField(
            model_name='matapelajaran',
            name='sekolah',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sekolah.sekolah'),
        ),
        migrations.AddField(
            model_name='tingkat',
            name='sekolah',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sekolah.sekolah'),
        ),
        migrations.AlterField(
            model_name='kelompokmapel',
            name='sekolah',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sekolah.sekolah'),
        ),
        migrations.AlterField(
            model_name='matapelajaran',
            name='kel_mapel',
            field=models.ForeignKey(blank=True, help_text='Kelompok Mata Pelajaran', null=True, on_delete=django.db.models.deletion.SET_NULL, to='akademik.kelompokmapel'),
        ),
    ]