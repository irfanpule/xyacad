# Generated by Django 4.0.6 on 2023-12-19 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pegawai', '0007_alter_presensi_options_alter_presensi_ket'),
    ]

    operations = [
        migrations.AddField(
            model_name='pegawai',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
