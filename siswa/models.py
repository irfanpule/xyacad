from django.db import models
from core.models import BaseModel


class Siswa(BaseModel):

    # Pegawai.JNS_KELAMIN.LAKI_LAKI.value to access laki_laki
    # Pegawai.JNS_KELAMIN.LAKI_LAKI.label to access Laki - laki
    class JNS_KELAMIN(models.TextChoices):
        LAKI_LAKI = "laki_laki", "Laki - laki"
        PEREMPUAN = "perempuan", "Perempuan"

    nama = models.CharField('Nama Lengkap', max_length=150)
    nis = models.CharField('NIS', max_length=100, unique=True)
    nisn = models.CharField('NISN', max_length=100, unique=True, blank=True, null=True)
    tempat_lahir = models.CharField('Templat Lahir', max_length=100)
    tgl_lahir = models.DateField('Tanggal Lahir')
    jns_kelamin = models.CharField('Jenis Kelamin', max_length=20, choices=JNS_KELAMIN.choices)
    alamat = models.TextField('Alamat', blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    telp_wa = models.CharField('Telp / WA', max_length=25, blank=True, null=True)
    foto = models.ImageField('Foto', blank=True, null=True)
    sekolah = models.ForeignKey("sekolah.Sekolah", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nama}"

    class Meta:
        verbose_name = "Siswa"
        verbose_name_plural = "Siswa"
