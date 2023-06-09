# Generated by Django 4.0.6 on 2022-07-14 01:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0003_gedung_ruangan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nama', models.CharField(max_length=150, verbose_name='Nama Jurusan')),
                ('kode', models.CharField(max_length=100, verbose_name='Kode Jurusan')),
                ('keahlian', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bidang Keahlian')),
                ('umum', models.CharField(blank=True, max_length=200, null=True, verbose_name='Kopetensi Umum')),
                ('khusus', models.CharField(blank=True, max_length=200, null=True, verbose_name='Kopetensi Khusus')),
                ('sekolah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekolah.sekolah')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nama', models.CharField(max_length=150, verbose_name='Nama Jurusan')),
                ('kode', models.CharField(max_length=100, verbose_name='Kode Jurusan')),
                ('jurusan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekolah.jurusan')),
                ('ruangan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekolah.ruangan')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
