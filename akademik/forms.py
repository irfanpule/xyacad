from django import forms
from django.db.models import Q
from akademik.models import TahunAkademik, Kurikulum, KelompokMapel, Tingkat, MataPelajaran, Jadwal
from sekolah.models import Jurusan, Kelas, Sekolah, Ruangan
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

    def clean(self):
        cleaned_data = super().clean()
        # cek jam mulai tidak boleh >=
        if cleaned_data['jam_mulai'] >= cleaned_data['jam_akhir']:
            raise forms.ValidationError("Jam mulai tidak boleh lebih besar atau sama dengan jam akhir")

        # filter berdasarkan (sekolah, tahun_ajaran, kelas, hari, jam_mulai, jam_akhir)
        jadwals = Jadwal.objects.filter(
            Q(jam_mulai__range=(cleaned_data['jam_mulai'], cleaned_data['jam_akhir'])) |
            Q(jam_akhir__range=(cleaned_data['jam_mulai'], cleaned_data['jam_akhir'])),
            sekolah=cleaned_data['sekolah'], tahun_ajaran=cleaned_data['tahun_ajaran'],
            hari=cleaned_data['hari'],
        )

        # cek apakah sudah ada kelas pada jadwal tersebut kelas=cleaned_data['kelas'],
        if jadwals.filter(kelas=cleaned_data['kelas']).exists():
            raise forms.ValidationError(f"Kelas tersebut ({cleaned_data['kelas']}) sudah "
                                        f"memiliki jadwal di hari dan jam yang beririsan")

        # cek apakah ruangan sudah terdaftar pada jadwal tersebut
        if jadwals.filter(ruangan=cleaned_data['ruangan']).exists():
            raise forms.ValidationError("Ruangan sudah memiliki jadwal di hari dan jam yang beririsan")

        # cek apakah guru sudah terdaftar pada jadwal tersebut
        if jadwals.filter(guru=cleaned_data['guru']).exists():
            raise forms.ValidationError("Guru sudah memiliki jadwal di hari dan jam yang beririsan")

        return cleaned_data


class JadwalCreateFilterForm(forms.Form):
    sekolah = forms.ModelChoiceField(queryset=Sekolah.objects.filter(aktif=True))
    tahun_ajaran = forms.ModelChoiceField(queryset=TahunAkademik.objects.all())


class JadwalShowWeeklyFilterForm(forms.Form):
    sekolah = forms.ModelChoiceField(
        queryset=Sekolah.objects.filter(aktif=True),
        widget=ModelSelect2Widget(
            model=Sekolah,
            search_fields=['nama__icontains']
        )
    )
    kelas = forms.ModelChoiceField(
        queryset=Kelas.objects.all(),
        widget=ModelSelect2Widget(
            model=Kelas,
            search_fields=['nama__icontains'],
            dependent_fields={'sekolah': 'sekolah'}
        )
    )
    tahun_ajaran = forms.ModelChoiceField(queryset=TahunAkademik.objects.all())
