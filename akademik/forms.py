from django import forms
from akademik.models import TahunAkademik, Kurikulum, KelompokMalep


class TahunAkademikForm(forms.ModelForm):
    class Meta:
        model = TahunAkademik
        fields = '__all__'


class KurikulumForm(forms.ModelForm):
    class Meta:
        model = Kurikulum
        fields = '__all__'


class KelompokMapelForm(forms.ModelForm):
    class Meta:
        model = KelompokMalep
        fields = '__all__'
