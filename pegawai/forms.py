from django import forms
from pegawai.models import StatusPegawai, JenisPTK, Golongan, JabatanStruktural, JabatanFungsional, Pegawai


class StatusPegawaiForm(forms.ModelForm):
    class Meta:
        model = StatusPegawai
        fields = '__all__'


class JenisPTKForm(forms.ModelForm):
    class Meta:
        model = JenisPTK
        fields = '__all__'


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
        }
