import sweetify
from django.urls import reverse
from core.views import DeleteView, ListView, CreateView, UpdateView, DetailView
from sekolah.models import Sekolah, Gedung, Ruangan, Jurusan, Kelas
from sekolah.forms import SekolahForm, GedungForm, RuanganForm, JurusanForm, KelasForm


class SekolahListView(ListView):
    model = Sekolah
    title_page = 'Data Sekolah'
    sub_title = 'Dapat menambahkan lebih dari 1 entitas sekolah'


class SekolahCreateView(CreateView):
    form_class = SekolahForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data sekolah'
    sub_title = 'Jika pada Yayasan/Instansi terdapat SD, SMP, SMA dapat tambahkan disini'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data sekolah", timer=5000)
        return reverse('sekolah:sekolah_list')


class SekolahUpdateView(UpdateView):
    model = Sekolah
    form_class = SekolahForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data sekolah'
    sub_title = 'Jika pada Yayasan/Instansi terdapat SD, SMP, SMA dapat tambahkan disini'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data sekolah", timer=5000)
        return reverse('sekolah:sekolah_list')


class SekolahDetailView(DetailView):
    model = Sekolah


class SekolahDeleteView(DeleteView):
    model = Sekolah

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data sekolah", timer=5000)
        return reverse('sekolah:sekolah_list')


class GedungListView(ListView):
    model = Gedung
    title_page = 'Data Gedung'
    sub_title = 'Digunakan untuk mendata gedung yang dimiliki oleh sekolah'


class GedungDetailView(DetailView):
    model = Gedung


class GedungUpdateView(UpdateView):
    model = Gedung
    form_class = GedungForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data gedung'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data gedung", timer=5000)
        return reverse('sekolah:gedung_list')


class GedungCreateView(CreateView):
    form_class = GedungForm
    model = Gedung
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data gedung'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data gedung", timer=5000)
        return reverse('sekolah:gedung_list')


class GedungDeleteView(DeleteView):
    model = Gedung

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data gedung", timer=5000)
        return reverse('sekolah:gedung_list')


class RuanganListView(ListView):
    model = Ruangan
    title_page = 'Data Ruangan'
    sub_title = 'Data dari ruangan dari gedung sekolah'


class RuanganDetailView(DetailView):
    model = Ruangan


class RuanganCreateView(CreateView):
    form_class = RuanganForm
    model = Ruangan
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data ruangan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data ruangan", timer=5000)
        return reverse('sekolah:ruangan_list')


class RuanganUpdateView(UpdateView):
    model = Ruangan
    form_class = RuanganForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data ruangan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data ruangan", timer=5000)
        return reverse('sekolah:ruangan_list')


class RuanganDeleteView(DeleteView):
    model = Ruangan

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data ruangan", timer=5000)
        return reverse('sekolah:ruangan_list')


class JurusanListView(ListView):
    model = Jurusan
    title_page = 'Data Jurusan'


class JurusanDetailView(DetailView):
    model = Jurusan


class JurusanCreateView(CreateView):
    form_class = JurusanForm
    model = Jurusan
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data jurusan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data jurusan", timer=5000)
        return reverse('sekolah:jurusan_list')


class JurusanUpdateView(UpdateView):
    model = Jurusan
    form_class = JurusanForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data jurusan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data jurusan", timer=5000)
        return reverse('sekolah:jurusan_list')


class JurusanDeleteView(DeleteView):
    model = Jurusan

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data jurusan", timer=5000)
        return reverse('sekolah:jurusan_list')


class KelasListView(ListView):
    model = Kelas
    title_page = 'Data Kelas'
    sub_title = 'Daftar kelas dari tiap ruangan dan jurusan'


class KelasDetailView(DetailView):
    model = Kelas


class KelasCreateView(CreateView):
    form_class = KelasForm
    model = Kelas
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data kelas'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data kelas", timer=5000)
        return reverse('sekolah:kelas_list')


class KelasUpdateView(UpdateView):
    model = Kelas
    form_class = KelasForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data kelas'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data kelas", timer=5000)
        return reverse('sekolah:kelas_list')


class KelasDeleteView(DeleteView):
    model = Kelas

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data kelas", timer=5000)
        return reverse('sekolah:kelas_list')
