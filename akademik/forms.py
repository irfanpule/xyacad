from django import forms
from akademik.models import TahunAkademik


class TahunAkademikForm(forms.ModelForm):
    class Meta:
        model = TahunAkademik
        fields = '__all__'
