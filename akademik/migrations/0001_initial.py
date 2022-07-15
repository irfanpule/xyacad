# Generated by Django 4.0.6 on 2022-07-14 03:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sekolah', '0005_alter_kelas_kode_alter_kelas_nama'),
        ('pegawai', '0003_alter_pegawai_tgl_masuk'),
    ]

    operations = [
        migrations.CreateModel(
            name='KelompokMalep',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nama', models.CharField(max_length=150, verbose_name='Nama Kelompok')),
                ('jenis', models.CharField(max_length=150, verbose_name='Jenis')),
                ('sekolah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekolah.sekolah')),
            ],
            options={
                'abstract': False,
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
                'abstract': False,
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
                'abstract': False,
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
                'abstract': False,
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
                ('kel_mapel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='akademik.kelompokmalep')),
                ('kurikulum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='akademik.kurikulum')),
                ('tingkat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akademik.tingkat')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]