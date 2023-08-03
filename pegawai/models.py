from django.db import models
from core.models import BaseModel
from sekolah.models import Sekolah


class Golongan(BaseModel):
    nama = models.CharField('Nama Golongan', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama}"


class JenisPTK(BaseModel):
    nama = models.CharField('Nama PTK', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama}"


class JabatanFungsional(BaseModel):
    nama = models.CharField('Nama Jabatan', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama}"


class JabatanStruktural(BaseModel):
    nama = models.CharField('Nama Jabatan', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama}"


class StatusPegawai(BaseModel):
    nama = models.CharField('Status', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama}"


class Pegawai(BaseModel):

    # Pegawai.JNS_KELAMIN.LAKI_LAKI.value to access laki_laki
    # Pegawai.JNS_KELAMIN.LAKI_LAKI.label to access Laki - laki
    class JNS_KELAMIN(models.TextChoices):
        LAKI_LAKI = "laki_laki", "Laki - laki"
        PEREMPUAN = "perempuan", "Perempuan"

    class PENDIDIKAN(models.TextChoices):
        SD = "sd", "SD"
        SMP = "smp", "SMP"
        SMA_SMK = "sma_smk", "SMA/SMK"
        D3 = "d3", "D3"
        S1 = "s1", "S1"
        S2 = "s2", "S2"

    nama = models.CharField('Nama Lengkap', max_length=150)
    nip = models.CharField('NIP / NIY', max_length=100)
    kode = models.CharField('Kode Pegawai', max_length=100)
    tempat_lahir = models.CharField('Templat Lahir', max_length=100)
    tgl_lahir = models.DateField('Tanggal Lahir')
    jns_kelamin = models.CharField('Jenis Kelamin', max_length=20, choices=JNS_KELAMIN.choices)
    pendidikan = models.CharField('Pendidikan Terakhir', max_length=20, choices=PENDIDIKAN.choices)
    alamat = models.TextField('Alamat (KTP)', blank=True, null=True)
    domisili = models.TextField('Alamat (Domisili)', blank=True, null=True)
    status = models.ForeignKey(StatusPegawai, on_delete=models.CASCADE)
    golongan = models.ForeignKey(Golongan, on_delete=models.CASCADE)
    jenis_ptk = models.ForeignKey(JenisPTK, on_delete=models.CASCADE)
    jabatan_fungsional = models.ForeignKey(JabatanFungsional, on_delete=models.CASCADE)
    jabatan_struktural = models.ForeignKey(JabatanStruktural, on_delete=models.CASCADE)
    no_sk = models.CharField('Nomor SK', max_length=150, blank=True, null=True)
    tmt_awal = models.CharField('TMT Awal', max_length=150, blank=True, null=True)
    tgl_masuk = models.DateField('Tanggal Masuk', blank=True, null=True)
    tempat_tugas = models.CharField('Tempat Tugas', max_length=150, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    telp_wa = models.CharField('Telp / WA', max_length=25, blank=True, null=True)
    foto = models.ImageField('Foto', blank=True, null=True)
    sekolah = models.ForeignKey(Sekolah, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nama}"
