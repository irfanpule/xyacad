import datetime

from django import forms
from django.contrib.auth import authenticate
from pegawai.models import StatusPegawai, JenisPTK, Golongan, JabatanStruktural, JabatanFungsional, Pegawai, Presensi
from django_flatpickr.widgets import DatePickerInput, DateTimePickerInput
from django_flatpickr.schemas import FlatpickrOptions
from django_select2.forms import Select2Widget


class StatusPegawaiForm(forms.ModelForm):
    class Meta:
        model = StatusPegawai
        fields = '__all__'
        help_texts = {
            'nama': 'Contoh: PPPK atau Honorer atau Kontrak atau PNS atau Tetap',
        }


class JenisPTKForm(forms.ModelForm):
    class Meta:
        model = JenisPTK
        fields = '__all__'
        help_texts = {
            'nama': 'Contoh: PTK diagnostik, PTK empiris'
        }


class GolonganForm(forms.ModelForm):
    class Meta:
        model = Golongan
        fields = '__all__'


class JabatanStrukturalForm(forms.ModelForm):
    class Meta:
        model = JabatanStruktural
        fields = '__all__'


class JabatanFungsionalForm(forms.ModelForm):
    class Meta:
        model = JabatanFungsional
        fields = '__all__'


class PegawaiForm(forms.ModelForm):
    class Meta:
        model = Pegawai
        exclude = ['user']
        widgets = {
            'alamat': forms.Textarea(attrs={'rows': 1}),
            'domisili': forms.Textarea(attrs={'rows': 1}),
            "tgl_lahir": DatePickerInput(options=FlatpickrOptions(maxDate="today")),
            "tgl_masuk": DatePickerInput(options=FlatpickrOptions(maxDate="today")),
            "golongan": Select2Widget,
            "jabatan_fungsional": Select2Widget,
            "jabatan_struktural": Select2Widget,
            "jenis_ptk": Select2Widget,
            "sekolah": Select2Widget,
            "status": Select2Widget,
        }


class PresensiHadirForm(forms.ModelForm):
    class Meta:
        model = Presensi
        fields = ['pegawai', 'clockin', 'clockout', 'ket']
        widgets = {
            'clockin': DateTimePickerInput(options=FlatpickrOptions(maxDate="today")),
            'clockout': DateTimePickerInput(options=FlatpickrOptions(maxDate="today"))
        }

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False)
        instance.status = Presensi.STATUS.hadir
        instance.save()
        return instance


class PresensiSakitForm(forms.ModelForm):
    class Meta:
        model = Presensi
        fields = ['pegawai', 'clockin', 'ket']
        help_texts = {
            'ket': 'Keterangan sakit. Lampirkan link Dokumen seperti Surat sakit.'
        }
        labels = {
            'clockin': 'Tanggal'
        }
        widgets = {
            'clockin': DatePickerInput(options=FlatpickrOptions(maxDate="today")),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ket'].required = True

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False)
        instance.status = Presensi.STATUS.sakit
        instance.clockout = instance.clockin
        instance.save()
        return instance


class PresensiIjinForm(PresensiSakitForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ket'].help_text = "Keterangan ijin."

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False)
        instance.status = Presensi.STATUS.ijin
        instance.clockout = instance.clockin
        instance.save()
        return instance


class PresensiCutiForm(PresensiSakitForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ket'].help_text = "Keterangan cuti"

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False)
        instance.status = Presensi.STATUS.cuti
        instance.clockout = instance.clockin
        instance.save()
        return instance


class PresensiClockInForm(forms.Form):
    nip = forms.CharField(help_text="Masukan NIP (Nomor Induk Pegawai)", label="NIP")
    password = forms.CharField(widget=forms.PasswordInput, label="Kata Sandi",
                               help_text="Masukan Kata Sandi untuk melanjutkan proses")

    def __init__(self, *args, **kwargs):
        self.pegawai = None
        self.presensi = None
        super().__init__(*args, **kwargs)

    def set_pegawai(self):
        try:
            self.pegawai = Pegawai.objects.get(nip=self.cleaned_data['nip'])
        except Pegawai.DoesNotExist:
            raise forms.ValidationError("Pegawai dengan NIP tersebut tidak ditemukan.", code='nip_404')

    def clean(self, edited=False):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        username = cleaned_data.get("nip")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("NIP atau Kata Sandi Anda tidak cocok.",
                                        code='user_404')

        if not edited:
            self.set_pegawai()
            if Presensi.objects.filter(pegawai=self.pegawai, clockin__day=datetime.datetime.now().day).exists():
                raise forms.ValidationError("Pegawai dengan NIP sudah melakukan clock in.",
                                            code='already_clockin')
        return cleaned_data

    def save(self, commit=True, *args, **kwargs):
        presensi = Presensi.objects.create(
            pegawai=self.pegawai,
            clockin=datetime.datetime.now(),
            status=Presensi.STATUS.hadir,
            ket="clock in mandiri"
        )
        return presensi


class PresensiClockOutForm(PresensiClockInForm):

    def clean(self):
        cleaned_data = super().clean(edited=True)
        self.set_pegawai()
        self.presensi = Presensi.objects.filter(
            pegawai=self.pegawai,
            clockin__day=datetime.datetime.now().day,
            clockout__isnull=True
        ).first()

        if not self.presensi:
            raise forms.ValidationError("Pegawai dengan NIP ini belum melakukan clock in.",
                                        code='not_yet_clockin')
        return cleaned_data

    def save(self, commit=True, *args, **kwargs):
        self.presensi.clockout = datetime.datetime.now()
        self.presensi.ket = self.presensi.ket + " clock out mandiri"
        self.presensi.save()
        return self.presensi


class PresensiAktifForm(forms.Form):
    nip = forms.CharField(help_text="Masukan NIP (Nomor Induk Pegawai)", label="NIP")
    password = forms.CharField(widget=forms.PasswordInput, label="Kata Sandi",
                               help_text="Masukan Kata Sandi untuk melanjutkan proses")

    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self, edited=False):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        username = cleaned_data.get("nip")
        self.user = authenticate(username=username, password=password)
        if not self.user:
            raise forms.ValidationError("NIP atau Kata Sandi Anda tidak cocok.",
                                        code='user_404')
        if not self.has_auth():
            raise forms.ValidationError("Hanya akun admin yang dapat mengaktifkan halaman presensi.",
                                        code='user_not_admin')
        return cleaned_data

    def has_auth(self):
        return self.user.is_authenticated and self.user.is_superuser
