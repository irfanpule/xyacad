from django import forms
from akademik.models import TahunAkademik, Kurikulum, KelompokMapel, Tingkat, MataPelajaran, Jadwal
from sekolah.models import Jurusan, Kelas, Sekolah, Gedung, Ruangan
from pegawai.models import Pegawai
from django_select2.forms import Select2Widget, ModelSelect2Widget
from django_flatpickr.widgets import TimePickerInput
from django_flatpickr.schemas import FlatpickrOptions


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kel_mapel'].required = True
        self.fields['kurikulum'].required = True


class JadwalForm(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = '__all__'
        widgets = {
            'jam_akhir': TimePickerInput(options=FlatpickrOptions(time_24hr=True)),
            'jam_mulai': TimePickerInput(options=FlatpickrOptions(time_24hr=True)),
            'tahun_ajaran': forms.HiddenInput(),
            'sekolah': forms.HiddenInput()
        }

    def __init__(self, sekolah=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kelas'].required = True
        self.fields['guru'].required = True
        self.fields['sekolah'].required = True
        self.fields['ruangan'].required = True

        if sekolah:
            self.fields['jurusan'].queryset = Jurusan.objects.filter(sekolah=sekolah)
            self.fields['kelas'].queryset = Kelas.objects.filter(sekolah=sekolah)
            self.fields['guru'].queryset = Pegawai.objects.filter(sekolah=sekolah)
            self.fields['mata_pelajaran'].queryset = MataPelajaran.objects.filter(kel_mapel__sekolah=sekolah)
            self.fields['ruangan'].queryset = Ruangan.objects.filter(gedung__sekolah=sekolah)


class JadwalCreateFilterForm(forms.Form):
    sekolah = forms.ModelChoiceField(queryset=Sekolah.objects.filter(aktif=True))
    tahun_ajaran = forms.ModelChoiceField(queryset=TahunAkademik.objects.all())


class JadwalShowWeeklyFilterForm(JadwalCreateFilterForm):
    pass
