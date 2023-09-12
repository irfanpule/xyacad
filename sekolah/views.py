import sweetify
from django.urls import reverse
from core.views import BaseDeleteView, ListBreadcrumbView, CreateBreadcrumbView, UpdateBreadcrumbView, DetailBreadcrumbView
from sekolah.models import Sekolah, Gedung, Ruangan, Jurusan, Kelas
from sekolah.forms import SekolahForm, GedungForm, RuanganForm, JurusanForm, KelasForm


class SekolahListView(ListBreadcrumbView):
    model = Sekolah
    title_page = 'Data Sekolah'
    sub_title = 'Dapat menambahkan lebih dari 1 entitas sekolah'


class SekolahCreateView(CreateBreadcrumbView):
    form_class = SekolahForm
    model = Sekolah
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah Data Sekolah'
    sub_title = 'Jika pada Yayasan/Instansi terdapat SD, SMP, SMA dapat tambahkan disini'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data sekolah", timer=5000)
        return reverse('sekolah:sekolah_list')


class SekolahUpdateView(UpdateBreadcrumbView):
    model = Sekolah
    form_class = SekolahForm
    template_name = 'forms/two-column-form.html'
    title_page = 'Edit data sekolah'
    sub_title = 'Jika pada Yayasan/Instansi terdapat SD, SMP, SMA dapat tambahkan disini'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data sekolah", timer=5000)
        return reverse('sekolah:sekolah_list')


class SekolahDetailView(DetailBreadcrumbView):
    model = Sekolah
    specific_sidebar_menu = 'sekolah/sidebar.html'


class SekolahDeleteView(BaseDeleteView):
    model = Sekolah

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data sekolah", timer=5000)
        return reverse('sekolah:sekolah_list')


class GedungListView(ListBreadcrumbView):
    model = Gedung
    title_page = 'Data Gedung'
    sub_title = 'Digunakan untuk mendata gedung yang dimiliki oleh sekolah'


class GedungDetailView(DetailBreadcrumbView):
    model = Gedung
    specific_sidebar_menu = 'sekolah/sidebar.html'


class GedungUpdateView(UpdateBreadcrumbView):
    model = Gedung
    form_class = GedungForm
    template_name = 'forms/one-column-form.html'
    title_page = 'Edit Data Gedung'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data gedung", timer=5000)
        return reverse('sekolah:gedung_list')


class GedungCreateView(CreateBreadcrumbView):
    form_class = GedungForm
    model = Gedung
    template_name = 'forms/one-column-form.html'
    title_page = 'Tambah Data Gedung'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data gedung", timer=5000)
        return reverse('sekolah:gedung_list')


class GedungDeleteView(BaseDeleteView):
    model = Gedung

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data gedung", timer=5000)
        return reverse('sekolah:gedung_list')


class RuanganListView(ListBreadcrumbView):
    model = Ruangan
    title_page = 'Data Ruangan'
    sub_title = 'Data dari ruangan dari gedung sekolah'


class RuanganDetailView(DetailBreadcrumbView):
    model = Ruangan
    specific_sidebar_menu = 'sekolah/sidebar.html'


class RuanganCreateView(CreateBreadcrumbView):
    form_class = RuanganForm
    model = Ruangan
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah data ruangan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data ruangan", timer=5000)
        return reverse('sekolah:ruangan_list')


class RuanganUpdateView(UpdateBreadcrumbView):
    model = Ruangan
    form_class = RuanganForm
    template_name = 'forms/two-column-form.html'
    title_page = 'Edit data ruangan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data ruangan", timer=5000)
        return reverse('sekolah:ruangan_list')


class RuanganDeleteView(BaseDeleteView):
    model = Ruangan

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data ruangan", timer=5000)
        return reverse('sekolah:ruangan_list')


class JurusanListView(ListBreadcrumbView):
    model = Jurusan
    title_page = 'Data Jurusan'


class JurusanDetailView(DetailBreadcrumbView):
    model = Jurusan
    specific_sidebar_menu = 'sekolah/sidebar.html'


class JurusanCreateView(CreateBreadcrumbView):
    form_class = JurusanForm
    model = Jurusan
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah data jurusan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data jurusan", timer=5000)
        return reverse('sekolah:jurusan_list')


class JurusanUpdateView(UpdateBreadcrumbView):
    model = Jurusan
    form_class = JurusanForm
    template_name = 'forms/two-column-form.html'
    title_page = 'Edit data jurusan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data jurusan", timer=5000)
        return reverse('sekolah:jurusan_list')


class JurusanDeleteView(BaseDeleteView):
    model = Jurusan

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data jurusan", timer=5000)
        return reverse('sekolah:jurusan_list')


class KelasListView(ListBreadcrumbView):
    model = Kelas
    title_page = 'Data Kelas'
    sub_title = 'Daftar kelas dari tiap ruangan dan jurusan'


class KelasDetailView(DetailBreadcrumbView):
    model = Kelas
    specific_sidebar_menu = 'sekolah/sidebar.html'


class KelasCreateView(CreateBreadcrumbView):
    form_class = KelasForm
    model = Kelas
    template_name = 'forms/two-column-form.html'
    title_page = 'Tambah data kelas'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data kelas", timer=5000)
        return reverse('sekolah:kelas_list')


class KelasUpdateView(UpdateBreadcrumbView):
    model = Kelas
    form_class = KelasForm
    template_name = 'forms/two-column-form.html'
    title_page = 'Edit data kelas'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data kelas", timer=5000)
        return reverse('sekolah:kelas_list')


class KelasDeleteView(BaseDeleteView):
    model = Kelas

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data kelas", timer=5000)
        return reverse('sekolah:kelas_list')
