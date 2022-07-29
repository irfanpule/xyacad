import sweetify
from django.urls import reverse
from core.views import ListView, CreateView, UpdateView, DeleteView, DetailView
from pegawai.models import StatusPegawai, JenisPTK, Golongan, JabatanStruktural, JabatanFungsional, Pegawai
from pegawai.forms import (
    StatusPegawaiForm, JenisPTKForm, GolonganForm, JabatanStrukturalForm, JabatanFungsionalForm, PegawaiForm
)


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


class GolonganListView(ListView):
    model = Golongan
    title_page = 'Data Golongan'


class GolonganCreateView(CreateView):
    form_class = GolonganForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data Golongan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data golongan", timer=5000)
        return reverse('pegawai:list_golongan')


class GolonganUpdateView(UpdateView):
    model = Golongan
    form_class = GolonganForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data golongan'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data golongan", timer=5000)
        return reverse('pegawai:list_golongan')


class GolonganDeleteView(DeleteView):
    model = Golongan

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data golongan", timer=5000)
        return reverse('pegawai:list_golongan')


class JabatanStrukturalListView(ListView):
    model = JabatanStruktural
    title_page = 'Data Jabatan Struktural'


class JabatanStrukturalCreateView(CreateView):
    form_class = JabatanStrukturalForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data jabatan struktural'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data jabatan struktural", timer=5000)
        return reverse('pegawai:list_struktural')


class JabatanStrukturalUpdateView(UpdateView):
    model = JabatanStruktural
    form_class = JabatanStrukturalForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data jabatan struktural'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data jabatan struktural", timer=5000)
        return reverse('pegawai:list_struktural')


class JabatanStrukturalDeleteView(DeleteView):
    model = JabatanStruktural

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data jabatan struktural", timer=5000)
        return reverse('pegawai:list_struktural')


class JabatanFungsionalListView(ListView):
    model = JabatanFungsional
    title_page = 'Data Jabatan Fungsional'


class JabatanFungsionalCreateView(CreateView):
    form_class = JabatanFungsionalForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data jabatan fungsional'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data jabatan fungsional", timer=5000)
        return reverse('pegawai:list_fungsional')


class JabatanFungsionalUpdateView(UpdateView):
    model = JabatanFungsional
    form_class = JabatanFungsionalForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data jabatan fungsional'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data jabatan fungsional", timer=5000)
        return reverse('pegawai:list_fungsional')


class JabatanFungsionalDeleteView(DeleteView):
    model = JabatanFungsional

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data jabatan fungsional", timer=5000)
        return reverse('pegawai:list_fungsional')


class PegawaiListView(ListView):
    model = Pegawai
    title_page = 'Data Pegawai'


class PegawaiCreateView(CreateView):
    form_class = PegawaiForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data pegawai'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data pegawai", timer=5000)
        return reverse('pegawai:list')


class PegawaiUpdateView(UpdateView):
    model = Pegawai
    form_class = PegawaiForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data pegawai'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data pegawai", timer=5000)
        return reverse('pegawai:list')


class PegawaiDetailView(DetailView):
    model = Pegawai

    def get_title_page(self):
        return "Detail Pegawai"
