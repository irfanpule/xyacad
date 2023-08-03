from django import forms
from akademik.models import TahunAkademik, Kurikulum, KelompokMapel, Tingkat, MataPelajaran


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
        model = KelompokMapel
        fields = '__all__'


class TingkatForm(forms.ModelForm):
    class Meta:
        model = Tingkat
        fields = '__all__'


class MataPelajaranForm(forms.ModelForm):
    class Meta:
        model = MataPelajaran
        fields = '__all__'
