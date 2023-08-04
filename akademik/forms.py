from django import forms
from akademik.models import TahunAkademik, Kurikulum, KelompokMapel, Tingkat, MataPelajaran
from django_select2.forms import Select2Widget


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
        widgets = {
            'tingkat': Select2Widget,
            'kel_mapel': Select2Widget,
            'guru': Select2Widget,
            'kurikulum': Select2Widget,
            'jurusan': Select2Widget
        }
