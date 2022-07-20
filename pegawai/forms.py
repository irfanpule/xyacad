from django import forms
from pegawai.models import StatusPegawai, JenisPTK, Golongan


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
