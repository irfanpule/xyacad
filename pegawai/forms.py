from django import forms
from pegawai.models import StatusPegawai, JenisPTK, Golongan, JabatanStruktural, JabatanFungsional, Pegawai
from django_flatpickr.widgets import DatePickerInput
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
