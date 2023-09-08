import sweetify
from django.urls import reverse

from core.mixin import FormFilterMixin
from core.views import (
    ListBreadcrumbView, CreateBreadcrumbView, UpdateBreadcrumbView, BaseDeleteView, DetailBreadcrumbView
)
from siswa.models import Siswa, SiswaKelas
from siswa.forms import SiswaForm, SiswaKelasForm, SiswaKelasCreateFilterForm


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
    title_page = 'Tambah data siswa'
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


class SiswaKelasListView(ListBreadcrumbView):
    model = SiswaKelas
    title_page = 'Data Siswa Kelas'


class SiswaKelasCreateView(FormFilterMixin, CreateBreadcrumbView):
    form_class = SiswaKelasForm
    form_filter = SiswaKelasCreateFilterForm
    model = SiswaKelas
    template_name = 'siswa/form_siswakelas.html'
    title_page = 'Tambah data siswa kelas'
    btn_submit_name = 'Simpan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context.get('sekolah') and context.get('tahun_ajaran'):
            context["additional_title"] = f"{context['sekolah']} {context['tahun_ajaran']}"
        return context

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        filter_fields = self.get_form_filter_fields()

        if filter_fields.get('sekolah'):
            kwargs = self.get_form_kwargs()
            filter_fields = self.get_form_filter_fields()
            kwargs['initial']['tahun_ajaran'] = filter_fields['tahun_ajaran']
            return form_class(sekolah=filter_fields['sekolah'], **kwargs)
        else:
            return None

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data siswa kelas", timer=5000)
        return reverse('siswa:siswakelas_list')


class SiswaKelasUpdateView(UpdateBreadcrumbView):
    model = SiswaKelas
    form_class = SiswaKelasForm
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah data siswa kelas'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data siswa", timer=5000)
        return reverse('siswa:siswakelas_list')


class SiswaKelasDetailView(DetailBreadcrumbView):
    model = SiswaKelas
    template_name = "siswa/siswa_detail.html"

    def get_title_page(self):
        return "Detail Siswa Kelas"


class SiswaKelasDeleteView(BaseDeleteView):
    model = SiswaKelas

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus siswa kelas", timer=5000)
        return reverse('siswa:siswakelas_list')


class SiswaIDCardView(DetailBreadcrumbView):
    model = Siswa
    template_name = "siswa/id_card.html"

    def get_title_page(self):
        return "Kartu Pelajar"
