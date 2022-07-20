from django import forms
from pegawai.models import StatusPegawai


class StatusPegawaiForm(forms.ModelForm):
    class Meta:
        model = StatusPegawai
        fields = '__all__'
