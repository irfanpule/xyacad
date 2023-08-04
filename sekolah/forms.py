from django import forms
from sekolah.models import Sekolah, Gedung, Ruangan, Jurusan, Kelas
from django_select2.forms import Select2Widget


class SekolahForm(forms.ModelForm):
    class Meta:
        model = Sekolah
        fields = '__all__'
        widgets = {
            'alamat': forms.Textarea(attrs={'rows': 1}),
        }
        help_texts = {
            'telp_wa': 'Awali dengan +62',
        }

    def clean_kode_pos(self):
        kode_pos = self.cleaned_data['kode_pos']
        if kode_pos.isalpha():
            raise forms.ValidationError('Kode Pos harus angka')
        return kode_pos


class GedungForm(forms.ModelForm):
    class Meta:
        model = Gedung
        exclude = ('aktif',)
        widgets = {
            'sekolah': Select2Widget
        }


class RuanganForm(forms.ModelForm):
    class Meta:
        model = Ruangan
        fields = '__all__'
        widgets = {
            'gedung': Select2Widget
        }


class JurusanForm(forms.ModelForm):
    class Meta:
        model = Jurusan
        fields = '__all__'
        widgets = {
            'sekolah': Select2Widget
        }


class KelasForm(forms.ModelForm):
    class Meta:
        model = Kelas
        fields = '__all__'
        widgets = {
            'ruangan': Select2Widget,
            'jurusan': Select2Widget
        }
