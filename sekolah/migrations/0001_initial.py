# Generated by Django 4.0.6 on 2022-07-14 00:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sekolah',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nama', models.CharField(max_length=150, verbose_name='Nama Sekolah')),
                ('npns', models.CharField(max_length=100, verbose_name='NPNS')),
                ('nss', models.CharField(max_length=100, verbose_name='NSS')),
                ('alamat', models.TextField(verbose_name='Alamat')),
                ('kode_pos', models.CharField(max_length=10, verbose_name='Kode Pos')),
                ('kecamatan', models.CharField(max_length=100, verbose_name='Kecamatan')),
                ('kabupaten', models.CharField(max_length=100, verbose_name='Kabupaten')),
                ('provinsi', models.CharField(max_length=100, verbose_name='Provinsi')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('telp_wa', models.CharField(max_length=25, verbose_name='Telp / WA')),
                ('aktif', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]