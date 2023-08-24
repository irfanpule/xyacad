# Generated by Django 4.0.6 on 2023-08-20 16:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sekolah', '0009_remove_kelas_ruangan_kelas_sekolah'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nama', models.CharField(max_length=150, verbose_name='Nama Lengkap')),
                ('nis', models.CharField(max_length=100, unique=True, verbose_name='NIS')),
                ('nisn', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='NISN')),
                ('tempat_lahir', models.CharField(max_length=100, verbose_name='Templat Lahir')),
                ('tgl_lahir', models.DateField(verbose_name='Tanggal Lahir')),
                ('jns_kelamin', models.CharField(choices=[('laki_laki', 'Laki - laki'), ('perempuan', 'Perempuan')], max_length=20, verbose_name='Jenis Kelamin')),
                ('alamat', models.TextField(blank=True, null=True, verbose_name='Alamat')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('telp_wa', models.CharField(blank=True, max_length=25, null=True, verbose_name='Telp / WA')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto')),
                ('sekolah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekolah.sekolah')),
            ],
            options={
                'verbose_name': 'Siswa',
                'verbose_name_plural': 'Siswa',
            },
        ),
    ]