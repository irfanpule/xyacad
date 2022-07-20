import sweetify
from django.urls import reverse
from core.views import ListView, CreateView, UpdateView, DeleteView
from pegawai.models import StatusPegawai, JenisPTK
from pegawai.forms import StatusPegawaiForm, JenisPTKForm


class StatusPegawaiListView(ListView):
    model = StatusPegawai
    title_page = 'Data Status Pegawai'


class StatusPegawaiCreateView(CreateView):
    form_class = StatusPegawaiForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data status pegawai'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data status pegawai", timer=5000)
        return reverse('pegawai:list_status')


class StatusPegawaiUpdateView(UpdateView):
    model = StatusPegawai
    form_class = StatusPegawaiForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data status pegawai'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data status pegawai", timer=5000)
        return reverse('pegawai:list_status')


class StatusPegawaiDeleteView(DeleteView):
    model = StatusPegawai

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data status pegawai", timer=5000)
        return reverse('pegawai:list_status')


class JenisPTKListView(ListView):
    model = JenisPTK
    title_page = 'Data Jenis PTK'


class JenisPTKCreateView(CreateView):
    form_class = JenisPTKForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data jenis PTK'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data Jenis PTK", timer=5000)
        return reverse('pegawai:list_ptk')


class JenisPTKUpdateView(UpdateView):
    model = JenisPTK
    form_class = JenisPTKForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data Jenis PTK'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data Jenis PTK", timer=5000)
        return reverse('pegawai:list_ptk')


class JenisPTKDeleteView(DeleteView):
    model = JenisPTK

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data Jenis PTK", timer=5000)
        return reverse('pegawai:list_ptk')
