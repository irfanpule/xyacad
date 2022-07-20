from django import forms
from pegawai.models import StatusPegawai, JenisPTK


class StatusPegawaiForm(forms.ModelForm):
    class Meta:
        model = StatusPegawai
        fields = '__all__'


class JenisPTKForm(forms.ModelForm):
    class Meta:
        model = JenisPTK
        fields = '__all__'
