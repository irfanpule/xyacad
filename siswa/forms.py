from django import forms

from akademik.models import TahunAkademik
from sekolah.models import Sekolah, Kelas
from siswa.models import Siswa, SiswaKelas, PresensiSiswa
from django_flatpickr.widgets import DatePickerInput
from django_flatpickr.schemas import FlatpickrOptions
from django_select2.forms import Select2Widget


class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = '__all__'
        widgets = {
            'alamat': forms.Textarea(attrs={'rows': 1}),
            "tgl_lahir": DatePickerInput(options=FlatpickrOptions(maxDate="today")),
            "sekolah": Select2Widget,
        }


class SiswaKelasForm(forms.ModelForm):
    class Meta:
        model = SiswaKelas
        fields = '__all__'
        widgets = {
            "tahun_ajaran": forms.HiddenInput(),
        }

    def __init__(self, sekolah=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if sekolah:
            self.fields['siswa'].queryset = Siswa.objects.filter(sekolah=sekolah)
            self.fields['kelas'].queryset = Kelas.objects.filter(sekolah=sekolah)


class SiswaKelasCreateFilterForm(forms.Form):
    sekolah = forms.ModelChoiceField(queryset=Sekolah.objects.filter(aktif=True))
    tahun_ajaran = forms.ModelChoiceField(queryset=TahunAkademik.objects.all())


class PresensiSiswaForm(forms.ModelForm):
    class Meta:
        model = PresensiSiswa
        exclude = ['jadwal',]
        widgets = {
            'siswa_kelas': forms.Select(attrs={'readonly': True})
        }


class PresensiSiswaUpdateForm(forms.ModelForm):
    id = forms.UUIDField(widget=forms.HiddenInput())

    class Meta:
        model = PresensiSiswa
        exclude = ['jadwal',]
        widgets = {
            'siswa_kelas': forms.Select(attrs={'readonly': True})
        }
