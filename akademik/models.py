from django.db import models
from core.models import BaseModel


class TahunAkademik(BaseModel):
    nama = models.CharField('Nama Tahun Akademik', max_length=150)
    kode = models.CharField('Kode Tahun Akademik', max_length=150, unique=True)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = "Tahun Akademik"
        verbose_name_plural = "Tahun Akademik"


class Tingkat(BaseModel):
    nama = models.CharField('Nama Tingkat', max_length=150)
    kode = models.CharField('Kode Tingkat', max_length=150, unique=True)
    sekolah = models.ForeignKey("sekolah.Sekolah", on_delete=models.SET_NULL, blank=True, null=True)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama} - {self.sekolah}"

    class Meta:
        verbose_name = "Tingkat"
        verbose_name_plural = "Tingkat"


class Kurikulum(BaseModel):
    nama = models.CharField('Nama Kurikulum', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = "Kurikulum"
        verbose_name_plural = "Kurikulum"


class KelompokMapel(BaseModel):
    nama = models.CharField('Nama Kelompok', max_length=150)
    jenis = models.CharField('Jenis', max_length=150)
    sekolah = models.ForeignKey("sekolah.Sekolah", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.nama} - {self.sekolah}"

    class Meta:
        verbose_name = "Kelompok Mata Pelajaran"
        verbose_name_plural = "Kelompok Mata Pelajaran"


class MataPelajaran(BaseModel):
    nama = models.CharField('Nama Mata Pelajaran', max_length=150)
    kode = models.CharField('Kode Mata Pelajaran', max_length=150, unique=True)
    tingkat = models.ForeignKey("akademik.Tingkat", on_delete=models.CASCADE)
    kel_mapel = models.ForeignKey("akademik.KelompokMapel", on_delete=models.SET_NULL, blank=True, null=True,
                                  help_text="Kelompok Mata Pelajaran")
    kurikulum = models.ForeignKey("akademik.Kurikulum", on_delete=models.SET_NULL, blank=True, null=True)
    umum = models.CharField('Kompetensi Umum', max_length=200, blank=True, null=True)
    khusus = models.CharField('Kompetensi Khusus', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = "Mata Pelajaran"
        verbose_name_plural = "Mata Pelajaran"


class Jadwal(BaseModel):
    class HARI(models.TextChoices):
        SENIN = "senin", "Senin"
        SELASA = "salasa", "Selasa"
        RABU = "rabu", "Rabu"
        KAMIS = "kamis", "Kamis"
        JUMAT = "jumat", "Jumat"
        SABTU = "sabtu", "Sabtu"
        MINGGU = "minggu", "Minggu"

    kelas = models.ForeignKey("sekolah.Kelas", on_delete=models.SET_NULL, blank=True, null=True)
    jurusan = models.ForeignKey("sekolah.Jurusan", on_delete=models.SET_NULL, blank=True, null=True)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    hari = models.CharField(max_length=15, choices=HARI.choices)
    jam_mulai = models.TimeField()
    jam_akhir = models.TimeField()
    guru = models.ForeignKey("pegawai.Pegawai", on_delete=models.SET_NULL, blank=True, null=True)
    tahun_ajaran = models.ForeignKey('akademik.TahunAkademik', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.kelas.nama} - {self.get_hari_display()}"

    class Meta:
        verbose_name = "Jadwal"
        verbose_name_plural = "Jadwal"
