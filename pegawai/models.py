import random

from django.contrib.auth import get_user_model
from django.db import models
from django.templatetags.static import static
from core.models import BaseModel


class Golongan(BaseModel):
    nama = models.CharField('Nama Golongan', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama}"

    class Meta:
        verbose_name = "Golongan"
        verbose_name_plural = "Golongan"


class JenisPTK(BaseModel):
    nama = models.CharField('Nama PTK', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama}"

    class Meta:
        verbose_name = "Jenis PTK"
        verbose_name_plural = "Jenis PTK"


class JabatanFungsional(BaseModel):
    nama = models.CharField('Nama Jabatan', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama}"

    class Meta:
        verbose_name = "Jabatan Fungsional"
        verbose_name_plural = "Jabatan Fungsional"


class JabatanStruktural(BaseModel):
    nama = models.CharField('Nama Jabatan', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama}"

    class Meta:
        verbose_name = "Jabatan Struktural"
        verbose_name_plural = "Jabatan Struktural"


class StatusPegawai(BaseModel):
    nama = models.CharField('Status', max_length=150)
    ket = models.CharField('Keterangan', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nama}"

    class Meta:
        verbose_name = "Status Pegawai"
        verbose_name_plural = "Status Pegawai"


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
    kode = models.CharField('Kode Pegawai', max_length=100, unique=True)
    tempat_lahir = models.CharField('Templat Lahir', max_length=100)
    tgl_lahir = models.DateField('Tanggal Lahir')
    jns_kelamin = models.CharField('Jenis Kelamin', max_length=20, choices=JNS_KELAMIN.choices)
    pendidikan = models.CharField('Pendidikan Terakhir', max_length=20, choices=PENDIDIKAN.choices)
    alamat = models.TextField('Alamat (KTP)', blank=True, null=True)
    domisili = models.TextField('Alamat (Domisili)', blank=True, null=True)
    status = models.ForeignKey("pegawai.StatusPegawai", on_delete=models.CASCADE)
    golongan = models.ForeignKey("pegawai.Golongan", on_delete=models.CASCADE)
    jenis_ptk = models.ForeignKey("pegawai.JenisPTK", on_delete=models.CASCADE)
    jabatan_fungsional = models.ForeignKey("pegawai.JabatanFungsional", on_delete=models.CASCADE)
    jabatan_struktural = models.ForeignKey("pegawai.JabatanStruktural", on_delete=models.CASCADE)
    no_sk = models.CharField('Nomor SK', max_length=150, blank=True, null=True)
    tmt_awal = models.CharField('TMT Awal', max_length=150, blank=True, null=True)
    tgl_masuk = models.DateField('Tanggal Masuk', blank=True, null=True)
    tempat_tugas = models.CharField('Tempat Tugas', max_length=150, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    telp_wa = models.CharField('Telp / WA', max_length=25, blank=True, null=True)
    foto = models.ImageField('Foto', blank=True, null=True)
    sekolah = models.ForeignKey("sekolah.Sekolah", on_delete=models.CASCADE)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.nama}"

    class Meta:
        verbose_name = "Pegawai"
        verbose_name_plural = "Pegawai"

    def save(self, *args, **kwargs):
        if not self.user:
            self.user = self.create_user()
        super().save(*args, **kwargs)

    def get_foto(self):
        if self.foto:
            return self.foto.url
        else:
            filename = f"{self.jns_kelamin}-{random.randint(1, 4)}.png"
            path = f"assets/images/avatars/{filename}"
            return static(path)

    def get_alamat(self):
        if self.alamat:
            return self.alamat
        if self.domisili:
            return self.domisili
        return "-"

    def create_user(self):
        user = get_user_model()
        obj = user.objects.create_user(
            username=self.nip,
            password=self.tgl_lahir.strftime("%Y%m%d")
        )
        return obj


class Presensi(BaseModel):
    class STATUS(models.TextChoices):
        hadir = "hadir", "Hadir"
        sakit = "sakit", "Sakit"
        ijin = "ijin", "Ijin"
        cuti = "cuti", "Cuti"
        absen = "absen", "Absen"

    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
    clockin = models.DateTimeField('Waktu Masuk', blank=True, null=True)
    clockout = models.DateTimeField('Waktu Keluar', blank=True, null=True)
    status = models.CharField('Status', max_length=10, choices=STATUS.choices)
    ket = models.TextField('Keterangan', help_text='Keterangan atau link ref dokumen',
                           blank=True, null=True, default='')

    def __str__(self):
        return f"{self.pegawai} - {self.status}"

    class Meta:
        verbose_name = "Presensi"
        verbose_name_plural = "Presensi"
