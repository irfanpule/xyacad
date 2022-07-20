from django import forms
from sekolah.models import Sekolah, Gedung


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
        fields = '__all__'
