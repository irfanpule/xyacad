import sweetify
from django.urls import reverse
from core.views import DeleteView, ListView, CreateView, UpdateView, DetailView
from sekolah.models import Sekolah, Gedung, Ruangan
from sekolah.forms import SekolahForm, GedungForm, RuanganForm


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
        return reverse('sekolah:list')


class SekolahUpdateView(UpdateView):
    model = Sekolah
    form_class = SekolahForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data sekolah'
    sub_title = 'Jika pada Yayasan/Instansi terdapat SD, SMP, SMA dapat tambahkan disini'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data sekolah", timer=5000)
        return reverse('sekolah:list')


class SekolahDetailView(DetailView):
    model = Sekolah


class SekolahDeleteView(DeleteView):
    model = Sekolah

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data sekolah", timer=5000)
        return reverse('sekolah:list')


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
        return reverse('sekolah:list_gedung')


class GedungCreateView(CreateView):
    form_class = GedungForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data gedung'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data gedung", timer=5000)
        return reverse('sekolah:list_gedung')


class GedungDeleteView(DeleteView):
    model = Gedung

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data gedung", timer=5000)
        return reverse('sekolah:list_gedung')


class RuanganListView(ListView):
    model = Ruangan
    title_page = 'Data Ruangan'
    sub_title = 'Data dari ruangan dari gedung sekolah'


class RuanganDetailView(DetailView):
    model = Ruangan


class RuanganCreateView(CreateView):
    form_class = RuanganForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data ruangan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data ruangan", timer=5000)
        return reverse('sekolah:list_ruangan')


class RuanganUpdateView(UpdateView):
    model = Ruangan
    form_class = RuanganForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data ruangan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data ruangan", timer=5000)
        return reverse('sekolah:list_ruangan')


class RuanganDeleteView(DeleteView):
    model = Ruangan

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data ruangan", timer=5000)
        return reverse('sekolah:list_ruangan')
