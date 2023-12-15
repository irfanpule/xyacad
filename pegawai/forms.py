from django import forms
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
        fields = '__all__'
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
