from django import forms
from siswa.models import Siswa
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
