import sweetify
from django.urls import reverse
from core.views import ListBreadcrumbView, CreateBreadcrumbView, UpdateBreadcrumbView, BaseDeleteView, DetailBreadcrumbView
from pegawai.models import StatusPegawai, JenisPTK, Golongan, JabatanStruktural, JabatanFungsional, Pegawai
from pegawai.forms import (
    StatusPegawaiForm, JenisPTKForm, GolonganForm, JabatanStrukturalForm, JabatanFungsionalForm, PegawaiForm
)


class StatusPegawaiListView(ListBreadcrumbView):
    model = StatusPegawai
    title_page = 'Data Status Pegawai'


class StatusPegawaiCreateView(CreateBreadcrumbView):
    form_class = StatusPegawaiForm
    model = StatusPegawai
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah data status pegawai'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data status pegawai", timer=5000)
        return reverse('pegawai:statuspegawai_list')


class StatusPegawaiUpdateView(UpdateBreadcrumbView):
    model = StatusPegawai
    form_class = StatusPegawaiForm
    template_name = 'forms/two-column-form.html'
    title_page = 'Edit data status pegawai'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data status pegawai", timer=5000)
        return reverse('pegawai:statuspegawai_list')


class StatusPegawaiDetailView(DetailBreadcrumbView):
    model = StatusPegawai

    def get_title_page(self):
        return "Detail Status Pegawai"


class StatusPegawaiDeleteView(BaseDeleteView):
    model = StatusPegawai

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data status pegawai", timer=5000)
        return reverse('pegawai:statuspegawai_list')


class JenisPTKListView(ListBreadcrumbView):
    model = JenisPTK
    title_page = 'Data Jenis PTK'


class JenisPTKCreateView(CreateBreadcrumbView):
    form_class = JenisPTKForm
    model = JenisPTK
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah data jenis PTK'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data Jenis PTK", timer=5000)
        return reverse('pegawai:jenisptk_list')


class JenisPTKUpdateView(UpdateBreadcrumbView):
    model = JenisPTK
    form_class = JenisPTKForm
    template_name = 'forms/two-column-form.html'
    title_page = 'Edit data Jenis PTK'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data Jenis PTK", timer=5000)
        return reverse('pegawai:jenisptk_list')


class JenisPTKDetailView(DetailBreadcrumbView):
    model = JenisPTK

    def get_title_page(self):
        return "Detail Jenis PTK"


class JenisPTKDeleteView(BaseDeleteView):
    model = JenisPTK

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data Jenis PTK", timer=5000)
        return reverse('pegawai:jenisptk_list')


class GolonganListView(ListBreadcrumbView):
    model = Golongan
    title_page = 'Data Golongan'


class GolonganCreateView(CreateBreadcrumbView):
    form_class = GolonganForm
    model = Golongan
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah data Golongan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data golongan", timer=5000)
        return reverse('pegawai:golongan_list')


class GolonganUpdateView(UpdateBreadcrumbView):
    model = Golongan
    form_class = GolonganForm
    template_name = 'forms/two-column-form.html'
    title_page = 'Edit data golongan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data golongan", timer=5000)
        return reverse('pegawai:golongan_list')


class GolonganDetailView(DetailBreadcrumbView):
    model = Golongan

    def get_title_page(self):
        return "Detail Golongan"


class GolonganDeleteView(BaseDeleteView):
    model = Golongan

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data golongan", timer=5000)
        return reverse('pegawai:golongan_list')


class JabatanStrukturalListView(ListBreadcrumbView):
    model = JabatanStruktural
    title_page = 'Data Jabatan Struktural'


class JabatanStrukturalCreateView(CreateBreadcrumbView):
    form_class = JabatanStrukturalForm
    model = JabatanStruktural
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah data jabatan struktural'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data jabatan struktural", timer=5000)
        return reverse('pegawai:jabatanstruktural_list')


class JabatanStrukturalUpdateView(UpdateBreadcrumbView):
    model = JabatanStruktural
    form_class = JabatanStrukturalForm
    template_name = 'forms/two-column-form.html'
    title_page = 'Edit data jabatan struktural'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data jabatan struktural", timer=5000)
        return reverse('pegawai:jabatanstruktural_list')


class JabatanStrukturalDetailView(DetailBreadcrumbView):
    model = JabatanStruktural

    def get_title_page(self):
        return "Detail Jabatan Struktural"


class JabatanStrukturalDeleteView(BaseDeleteView):
    model = JabatanStruktural

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data jabatan struktural", timer=5000)
        return reverse('pegawai:jabatanstruktural_list')


class JabatanFungsionalListView(ListBreadcrumbView):
    model = JabatanFungsional
    title_page = 'Data Jabatan Fungsional'


class JabatanFungsionalCreateView(CreateBreadcrumbView):
    form_class = JabatanFungsionalForm
    model = JabatanFungsional
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah data jabatan fungsional'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data jabatan fungsional", timer=5000)
        return reverse('pegawai:jabatanfungsional_list')


class JabatanFungsionalUpdateView(UpdateBreadcrumbView):
    model = JabatanFungsional
    form_class = JabatanFungsionalForm
    template_name = 'forms/two-column-form.html'
    title_page = 'Edit data jabatan fungsional'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data jabatan fungsional", timer=5000)
        return reverse('pegawai:jabatanfungsional_list')


class JabatanFungsionalDetailView(DetailBreadcrumbView):
    model = JabatanFungsional

    def get_title_page(self):
        return "Detail Jabatan Fungsional"


class JabatanFungsionalDeleteView(BaseDeleteView):
    model = JabatanFungsional

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data jabatan fungsional", timer=5000)
        return reverse('pegawai:jabatanfungsional_list')


class PegawaiListView(ListBreadcrumbView):
    model = Pegawai
    title_page = 'Data Pegawai'


class PegawaiCreateView(CreateBreadcrumbView):
    form_class = PegawaiForm
    model = Pegawai
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah data pegawai'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data pegawai", timer=5000)
        return reverse('pegawai:pegawai_list')


class PegawaiUpdateView(UpdateBreadcrumbView):
    model = Pegawai
    form_class = PegawaiForm
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah data pegawai'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data pegawai", timer=5000)
        return reverse('pegawai:pegawai_list')


class PegawaiDetailView(DetailBreadcrumbView):
    model = Pegawai
    template_name = "pegawai/pegawai_detail.html"

    def get_title_page(self):
        return "Detail Pegawai"


class PegawaiIDCardView(DetailBreadcrumbView):
    model = Pegawai
    template_name = "pegawai/id_card.html"

    def get_title_page(self):
        return "Kartu Pagawai"
