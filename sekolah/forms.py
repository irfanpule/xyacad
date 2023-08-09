from django import forms
from sekolah.models import Sekolah, Gedung, Ruangan, Jurusan, Kelas
from django_select2.forms import Select2Widget


class SekolahForm(forms.ModelForm):
    class Meta:
        model = Sekolah
        fields = '__all__'
        widgets = {
            'alamat': forms.Textarea(attrs={'rows': 1}),
        }
        help_texts = {
            'nama': 'Contoh: SD IT Al-Furqon atau SMP N 1 Gedong Tataan',
            'telp_wa': 'Awali dengan +62',
            'nss': 'Nomor Statistik Sekolah'
        }

    def clean_kode_pos(self):
        kode_pos = self.cleaned_data['kode_pos']
        if kode_pos.isalpha():
            raise forms.ValidationError('Kode Pos harus angka')
        return kode_pos


class GedungForm(forms.ModelForm):
    class Meta:
        model = Gedung
        exclude = ('aktif',)
        widgets = {
            'sekolah': Select2Widget
        }
        help_texts = {
            'nama': 'Contoh: Gedung A atau Gedung 1 atau Blok A',
            'kode': 'Contoh: GDA atau GD1 atau G01BA (sesuai ketentuan sekolah)',
            'sekolah': 'Gedung ini berada pada sekolah mana'
        }


class RuanganForm(forms.ModelForm):
    class Meta:
        model = Ruangan
        fields = '__all__'
        widgets = {
            'gedung': Select2Widget
        }
        help_texts = {
            'nama': 'Contoh: Melati atau Anggrek atau Ruang 01',
            'kode': 'Contoh: Angger atau ANGR atau RK01 (sesuai ketentuan sekolah)',
        }


class JurusanForm(forms.ModelForm):
    class Meta:
        model = Jurusan
        fields = '__all__'
        widgets = {
            'sekolah': Select2Widget
        }
        help_texts = {
            'nama': 'Contoh: Ilmu Pengetahuan Alam atau Desain Komunikasi Visual',
            'kode': 'Contoh: IPA atau DKV'
        }


class KelasForm(forms.ModelForm):
    class Meta:
        model = Kelas
        fields = '__all__'
        widgets = {
            'ruangan': Select2Widget,
            'jurusan': Select2Widget
        }
        help_texts = {
            'nama': 'Contoh: Kelas 3 atau Kelas III',
            'kode': 'Contoh: KLS3 atau KLSIII',
            'jurusan': 'Pilih jika kelas tsb memiliki jurusan'
        }


class SekolahChoiceForm(forms.Form):
    sekolah = forms.ModelChoiceField(queryset=Sekolah.objects.filter(aktif=True))