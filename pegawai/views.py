import sweetify
from django.urls import reverse
from core.views import ListView, CreateView, UpdateView, DeleteView, DetailView
from pegawai.models import StatusPegawai, JenisPTK, Golongan, JabatanStruktural, JabatanFungsional, Pegawai
from pegawai.forms import (
    StatusPegawaiForm, JenisPTKForm, GolonganForm, JabatanStrukturalForm, JabatanFungsionalForm, PegawaiForm
)
from view_breadcrumbs import ListBreadcrumbMixin, CreateBreadcrumbMixin, UpdateBreadcrumbMixin, DetailBreadcrumbMixin


class StatusPegawaiListView(ListBreadcrumbMixin, ListView):
    model = StatusPegawai
    title_page = 'Data Status Pegawai'


class StatusPegawaiCreateView(CreateBreadcrumbMixin, CreateView):
    form_class = StatusPegawaiForm
    model = StatusPegawai
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data status pegawai'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data status pegawai", timer=5000)
        return reverse('pegawai:status_list')


class StatusPegawaiUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = StatusPegawai
    form_class = StatusPegawaiForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data status pegawai'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data status pegawai", timer=5000)
        return reverse('pegawai:statuspegawai_list')


class StatusPegawaiDetailView(DetailBreadcrumbMixin, DetailView):
    model = StatusPegawai
    template_name = 'general_detail.html'

    def get_title_page(self):
        return "Detail Status Pegawai"


class StatusPegawaiDeleteView(DeleteView):
    model = StatusPegawai

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data status pegawai", timer=5000)
        return reverse('pegawai:statuspegawai_list')


class JenisPTKListView(ListBreadcrumbMixin, ListView):
    model = JenisPTK
    title_page = 'Data Jenis PTK'


class JenisPTKCreateView(CreateBreadcrumbMixin, CreateView):
    form_class = JenisPTKForm
    model = JenisPTK
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data jenis PTK'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data Jenis PTK", timer=5000)
        return reverse('pegawai:jenisptk_list')


class JenisPTKUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = JenisPTK
    form_class = JenisPTKForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data Jenis PTK'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data Jenis PTK", timer=5000)
        return reverse('pegawai:jenisptk_list')


class JenisPTKDetailView(DetailBreadcrumbMixin, DetailView):
    model = JenisPTK
    template_name = 'general_detail.html'

    def get_title_page(self):
        return "Detail Jenis PTK"


class JenisPTKDeleteView(DeleteView):
    model = JenisPTK

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data Jenis PTK", timer=5000)
        return reverse('pegawai:jenisptk_list')


class GolonganListView(ListBreadcrumbMixin, ListView):
    model = Golongan
    title_page = 'Data Golongan'


class GolonganCreateView(CreateBreadcrumbMixin, CreateView):
    form_class = GolonganForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data Golongan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data golongan", timer=5000)
        return reverse('pegawai:golongan_list')


class GolonganUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Golongan
    form_class = GolonganForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data golongan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data golongan", timer=5000)
        return reverse('pegawai:golongan_list')


class GolonganDetailView(DetailBreadcrumbMixin, DetailView):
    model = Golongan
    template_name = 'general_detail.html'

    def get_title_page(self):
        return "Detail Golongan"


class GolonganDeleteView(DeleteView):
    model = Golongan

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data golongan", timer=5000)
        return reverse('pegawai:golongan_list')


class JabatanStrukturalListView(ListBreadcrumbMixin, ListView):
    model = JabatanStruktural
    title_page = 'Data Jabatan Struktural'


class JabatanStrukturalCreateView(CreateBreadcrumbMixin, CreateView):
    form_class = JabatanStrukturalForm
    model = JabatanStruktural
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data jabatan struktural'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data jabatan struktural", timer=5000)
        return reverse('pegawai:jabatanstruktural_list')


class JabatanStrukturalUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = JabatanStruktural
    form_class = JabatanStrukturalForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data jabatan struktural'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data jabatan struktural", timer=5000)
        return reverse('pegawai:jabatanstruktural_list')


class JabatanStrukturalDetailView(DetailBreadcrumbMixin, DetailView):
    model = JabatanStruktural
    template_name = 'general_detail.html'

    def get_title_page(self):
        return "Detail Jabatan Struktural"


class JabatanStrukturalDeleteView(DeleteView):
    model = JabatanStruktural

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data jabatan struktural", timer=5000)
        return reverse('pegawai:jabatanstruktural_list')


class JabatanFungsionalListView(ListBreadcrumbMixin, ListView):
    model = JabatanFungsional
    title_page = 'Data Jabatan Fungsional'


class JabatanFungsionalCreateView(CreateBreadcrumbMixin, CreateView):
    form_class = JabatanFungsionalForm
    model = JabatanFungsional
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data jabatan fungsional'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data jabatan fungsional", timer=5000)
        return reverse('pegawai:jabatanfungsional_list')


class JabatanFungsionalUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = JabatanFungsional
    form_class = JabatanFungsionalForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data jabatan fungsional'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data jabatan fungsional", timer=5000)
        return reverse('pegawai:jabatanfungsional_list')


class JabatanFungsionalDetailView(DetailBreadcrumbMixin, DetailView):
    model = JabatanFungsional
    template_name = 'general_detail.html'

    def get_title_page(self):
        return "Detail Jabatan Fungsional"


class JabatanFungsionalDeleteView(DeleteView):
    model = JabatanFungsional

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data jabatan fungsional", timer=5000)
        return reverse('pegawai:jabatanfungsional_list')


class PegawaiListView(ListBreadcrumbMixin, ListView):
    model = Pegawai
    title_page = 'Data Pegawai'


class PegawaiCreateView(CreateBreadcrumbMixin, CreateView):
    form_class = PegawaiForm
    model = Pegawai
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data pegawai'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data pegawai", timer=5000)
        return reverse('pegawai:pegawai_list')


class PegawaiUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Pegawai
    form_class = PegawaiForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data pegawai'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data pegawai", timer=5000)
        return reverse('pegawai:pegawai_list')


class PegawaiDetailView(DetailBreadcrumbMixin, DetailView):
    model = Pegawai

    def get_title_page(self):
        return "Detail Pegawai"
