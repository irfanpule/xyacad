import random

from django.contrib.auth import get_user_model
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

    class Meta:
        verbose_name = "Siswa Kelas"
        verbose_name_plural = "Siswa Kelas"


class ArsipSiswaKelas(BaseModel):
    """
    Model ini digunakan untuk mencatat riwayat / arsip dari jenjang kenaikan kelas siswa
    """
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    kelas = models.ForeignKey("sekolah.Kelas", on_delete=models.CASCADE)
    tahun_ajaran = models.ForeignKey("akademik.TahunAkademik", on_delete=models.CASCADE, blank=True, null=True)
    ket = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Arsip Siswa Kelas"
        verbose_name_plural = "Arsip Siswa kelas"


    def __str__(self):
        return f"{self.siswa} - {self.kelas}"


class PresensiSiswa(BaseModel):
    """
    Model ini digunakan untuk mencatat Presensi Siswa Kelas berdasarkan Jadwal
    """
    class STATUS(models.TextChoices):
        HADIR = "hadir", "Hadir"
        ABSEN = "absen", "Absen"
        IJIN = "ijin", "Ijin"
        SAKIT = "sakit", "Sakit"

    jadwal = models.ForeignKey("akademik.Jadwal", on_delete=models.CASCADE)
    siswa_kelas = models.ForeignKey(SiswaKelas, on_delete=models.CASCADE)
    status = models.CharField(max_length=6, choices=STATUS.choices, default=STATUS.ABSEN.value)

    class Meta:
        verbose_name = "Presensi Siswa"
        verbose_name_plural = "Presensi Siswa"

    def __str__(self):
        return f"{self.jadwal} - {self.siswa_kelas}"


class PresensiSiswaHarian(BaseModel):
    """
    Model ini digunakan untuk mencatat presensi siswa dalam satu aksi
    """
    jadwal = models.ForeignKey("akademik.Jadwal", on_delete=models.CASCADE)
    presensi_siswa = models.ManyToManyField(PresensiSiswa)
    ket = models.TextField("Keterangan", null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Presensi Siswa Harian"
        verbose_name_plural = "Presensi Siswa Harian"

    def __str__(self):
        return f"{self.jadwal} - {self.created}"
