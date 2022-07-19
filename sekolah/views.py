import sweetify
from django.urls import reverse
from core.views import DeleteView, ListView, CreateView, UpdateView, DetailView
from sekolah.models import Sekolah
from sekolah.forms import SekolahForm


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
