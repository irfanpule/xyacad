import sweetify
from django.urls import reverse
from core.views import (
    ListBreadcrumbView, CreateBreadcrumbView, UpdateBreadcrumbView, BaseDeleteView, DetailBreadcrumbView
)
from siswa.models import Siswa
from siswa.forms import SiswaForm


class SiswaListView(ListBreadcrumbView):
    model = Siswa
    title_page = 'Data Siswa'


class SiswaCreateView(CreateBreadcrumbView):
    form_class = SiswaForm
    model = Siswa
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah data siswa'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data siswa", timer=5000)
        return reverse('siswa:siswa_list')


class SiswaUpdateView(UpdateBreadcrumbView):
    model = Siswa
    form_class = SiswaForm
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah data pegawai'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data siswa", timer=5000)
        return reverse('siswa:siswa_list')


class SiswaDetailView(DetailBreadcrumbView):
    model = Siswa
    template_name = "siswa/siswa_detail.html"

    def get_title_page(self):
        return "Detail Siswa"


class SiswaDeleteView(BaseDeleteView):
    model = Siswa

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus siswa", timer=5000)
        return reverse('siswa:siswa_list')