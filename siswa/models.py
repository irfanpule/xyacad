import random

from django.db import models
from core.models import BaseModel
from django.templatetags.static import static


class Siswa(BaseModel):
    """
    Model ini digunakan untuk menyimpan data Siswa
    """
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
        return f"{self.nama} - {self.nis}"

    class Meta:
        verbose_name = "Siswa"
        verbose_name_plural = "Siswa"

    def get_foto(self):

        if self.foto:
            return self.foto.url
        else:
            filename = f"{self.jns_kelamin}-{random.randint(1, 4)}.png"
            path = f"assets/images/avatars/{filename}"
            return static(path)


class SiswaKelas(BaseModel):
    """
    model ini digunakan untuk mencatat siswa tersebut berada kelas mana
    """
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE)
    kelas = models.ForeignKey("sekolah.Kelas", on_delete=models.CASCADE)
    tahun_ajaran = models.ForeignKey("akademik.TahunAkademik", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.siswa} - {self.kelas}"


class ArsipSiswaKelas(BaseModel):
    """
    Model ini digunakan untuk mencatat riwayat / arsip dari jenjang kenaikan kelas siswa
    """
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    kelas = models.ForeignKey("sekolah.Kelas", on_delete=models.CASCADE)
    tahun_ajaran = models.ForeignKey("akademik.TahunAkademik", on_delete=models.CASCADE, blank=True, null=True)
    ket = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.siswa} - {self.kelas}"
