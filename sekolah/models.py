from django.db import models
from core.models import BaseModel


class Sekolah(BaseModel):
    nama = models.CharField('Nama Sekolah', max_length=150)
    npns = models.CharField('NPNS', max_length=100, blank=True, null=True)
    nss = models.CharField('NSS', max_length=100, blank=True, null=True)
    alamat = models.TextField('Alamat')
    kode_pos = models.CharField('Kode Pos', max_length=10)
    kecamatan = models.CharField('Kecamatan', max_length=100)
    kabupaten = models.CharField('Kabupaten', max_length=100)
    provinsi = models.CharField('Provinsi', max_length=100)
    email = models.EmailField('Email', blank=True, null=True)
    telp_wa = models.CharField('Telp / WA', max_length=25, blank=True, null=True)
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nama} - {self.id}"


class Gedung(BaseModel):
    nama = models.CharField('Nama Gedung', max_length=150)
    kode = models.CharField('Kode Gedung', max_length=100)
    jml_lantai = models.PositiveSmallIntegerField('Jumlah Lantai', default=1)
    panjang = models.FloatField('Panjang Gedung', help_text='satuan dalam meter (m)', blank=True, null=True)
    lebar = models.FloatField('Lebar Gedung', help_text='satuan dalam meter (m)', blank=True, null=True)
    tinggi = models.FloatField('Tinggi Gedung', help_text='satuan dalam meter (m)', blank=True, null=True)
    aktif = models.BooleanField(default=True)
    sekolah = models.ForeignKey(Sekolah, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nama} - {self.id}"


class Ruangan(BaseModel):
    nama = models.CharField('Nama Ruangan', max_length=150)
    kode = models.CharField('Kode Ruangan', max_length=100)
    kapasitas_belajar = models.PositiveSmallIntegerField('Kapasitas Belajar', default=0)
    kapasitas_ujian = models.PositiveSmallIntegerField('Kapasitas Ujian', default=0)
    gedung = models.ForeignKey(Gedung, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nama} - {self.id}"


class Jurusan(BaseModel):
    nama = models.CharField('Nama Jurusan', max_length=150)
    kode = models.CharField('Kode Jurusan', max_length=100)
    keahlian = models.CharField('Bidang Keahlian', max_length=200, blank=True, null=True)
    umum = models.CharField('Kopetensi Umum', max_length=200, blank=True, null=True)
    khusus = models.CharField('Kopetensi Khusus', max_length=200, blank=True, null=True)
    sekolah = models.ForeignKey(Sekolah, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nama} - {self.id}"


class Kelas(BaseModel):
    nama = models.CharField('Nama Kelas', max_length=150)
    kode = models.CharField('Kode Kelas', max_length=100)
    ruangan = models.ForeignKey(Ruangan, on_delete=models.CASCADE)
    jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nama} - {self.id}"
