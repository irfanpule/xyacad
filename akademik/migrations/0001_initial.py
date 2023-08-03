# Generated by Django 4.0.6 on 2023-08-03 04:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pegawai', '0004_alter_golongan_options_and_more'),
        ('sekolah', '0006_alter_gedung_options_alter_jurusan_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KelompokMapel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nama', models.CharField(max_length=150, verbose_name='Nama Kelompok')),
                ('jenis', models.CharField(max_length=150, verbose_name='Jenis')),
                ('sekolah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekolah.sekolah')),
            ],
            options={
                'verbose_name': 'Kelompok Mata Pelajaran',
                'verbose_name_plural': 'Kelompok Mata Pelajaran',
            },
        ),
        migrations.CreateModel(
            name='Kurikulum',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nama', models.CharField(max_length=150, verbose_name='Nama Kurikulum')),
                ('ket', models.CharField(blank=True, max_length=100, null=True, verbose_name='Keterangan')),
            ],
            options={
                'verbose_name': 'Kurikulum',
                'verbose_name_plural': 'Kurikulum',
            },
        ),
        migrations.CreateModel(
            name='TahunAkademik',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nama', models.CharField(max_length=150, verbose_name='Nama Tahun Akademik')),
                ('kode', models.CharField(max_length=150, verbose_name='Kode Tahun Akademik')),
                ('ket', models.CharField(blank=True, max_length=100, null=True, verbose_name='Keterangan')),
            ],
            options={
                'verbose_name': 'Tahun Akademik',
                'verbose_name_plural': 'Tahun Akademik',
            },
        ),
        migrations.CreateModel(
            name='Tingkat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nama', models.CharField(max_length=150, verbose_name='Nama Tingkat')),
                ('kode', models.CharField(max_length=150, verbose_name='Kode Tingkat')),
                ('ket', models.CharField(blank=True, max_length=100, null=True, verbose_name='Keterangan')),
            ],
            options={
                'verbose_name': 'Tingkat',
                'verbose_name_plural': 'Tingkat',
            },
        ),
        migrations.CreateModel(
            name='MataPelajaran',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nama', models.CharField(max_length=150, verbose_name='Nama Mata Pelajaran')),
                ('kode', models.CharField(max_length=150, verbose_name='Kode Mata Pelajaran')),
                ('jml_jam', models.PositiveSmallIntegerField(verbose_name='Jumlah Jam')),
                ('umum', models.CharField(max_length=200, verbose_name='Kompetensi Umum')),
                ('khusu', models.CharField(max_length=200, verbose_name='Kompetensi Khusus')),
                ('guru', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pegawai.pegawai')),
                ('jurusan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sekolah.jurusan')),
                ('kel_mapel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='akademik.kelompokmapel')),
                ('kurikulum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='akademik.kurikulum')),
                ('tingkat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akademik.tingkat')),
            ],
            options={
                'verbose_name': 'Mata Pelajaran',
                'verbose_name_plural': 'Mata Pelajaran',
            },
        ),
    ]
