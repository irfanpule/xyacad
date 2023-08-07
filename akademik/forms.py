from django import forms
from akademik.models import TahunAkademik, Kurikulum, KelompokMapel, Tingkat, MataPelajaran
from django_select2.forms import Select2Widget


class TahunAkademikForm(forms.ModelForm):
    class Meta:
        model = TahunAkademik
        fields = '__all__'
        help_texts = {
            'nama': 'Contoh: 2023/2024',
            'kode': 'Contoh: TA2324'
        }


class KurikulumForm(forms.ModelForm):
    class Meta:
        model = Kurikulum
        fields = '__all__'
        help_texts = {
            'nama': 'Contoh: Kurikulum 13, Kurikulum Merdeka',
        }


class KelompokMapelForm(forms.ModelForm):
    class Meta:
        model = KelompokMapel
        fields = '__all__'
        help_texts = {
            'nama': 'Contoh: Kelompok Umum, Kelompok Kejuruan, Kelompok A, Kelompok B',
        }


class TingkatForm(forms.ModelForm):
    class Meta:
        model = Tingkat
        fields = '__all__'
        help_texts = {
            'nama': 'Contoh: Tingkat 1 atau Tingkat 12',
            'kode': 'Contoh: 1 atau I atau 12 atau XII atau T12 (sesuai ketentuan sekolah)',
            'sekolah': 'Pilih tingkat tersebut untuk sekolah mana.'
        }


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
        labels = {
            'kel_mapel': 'Kelompok MaPel'
        }
        help_texts = {
            'nama': 'Contoh: Matematika, Seni Budaya, Biologi',
            'kode': 'Contoh: MTK, SB, BIO (sesuai ketentuan sekolah)'
        }
