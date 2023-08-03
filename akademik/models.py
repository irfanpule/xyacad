from django.db import models
from core.models import BaseModel
from sekolah.models import Sekolah, Jurusan
from pegawai.models import Pegawai


class TahunAkademik(BaseModel):
    nama = models.CharField('Nama Tahun Akademik', max_length=150)
    kode = models.CharField('Kode Tahun Akademik', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama} - {self.id}"

    class Meta:
        verbose_name = "Tahun Akademik"
        verbose_name_plural = "Tahun Akademik"


class Tingkat(BaseModel):
    nama = models.CharField('Nama Tingkat', max_length=150)
    kode = models.CharField('Kode Tingkat', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama} - {self.id}"

    class Meta:
        verbose_name = "Tingkat"
        verbose_name_plural = "Tingkat"


class Kurikulum(BaseModel):
    nama = models.CharField('Nama Kurikulum', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama} - {self.id}"

    class Meta:
        verbose_name = "Kurikulum"
        verbose_name_plural = "Kurikulum"


class KelompokMapel(BaseModel):
    nama = models.CharField('Nama Kelompok', max_length=150)
    jenis = models.CharField('Jenis', max_length=150)
    sekolah = models.ForeignKey(Sekolah, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nama} - {self.id}"

    class Meta:
        verbose_name = "Kelompok Mata Pelajaran"
        verbose_name_plural = "Kelompok Mata Pelajaran"


class MataPelajaran(BaseModel):
    nama = models.CharField('Nama Mata Pelajaran', max_length=150)
    kode = models.CharField('Kode Mata Pelajaran', max_length=150)
    jml_jam = models.PositiveSmallIntegerField('Jumlah Jam')
    tingkat = models.ForeignKey(Tingkat, on_delete=models.CASCADE)
    kel_mapel = models.ForeignKey(KelompokMapel, on_delete=models.SET_NULL, blank=True, null=True)
    jurusan = models.ForeignKey(Jurusan, on_delete=models.SET_NULL, blank=True, null=True)
    guru = models.ForeignKey(Pegawai, on_delete=models.SET_NULL, blank=True, null=True)
    kurikulum = models.ForeignKey(Kurikulum, on_delete=models.SET_NULL, blank=True, null=True)
    umum = models.CharField('Kompetensi Umum', max_length=200)
    khusu = models.CharField('Kompetensi Khusus', max_length=200)

    def __str__(self):
        return f"{self.nama} - {self.id}"

    class Meta:
        verbose_name = "Mata Pelajaran"
        verbose_name_plural = "Mata Pelajaran"
