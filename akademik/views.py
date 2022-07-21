import sweetify
from django.urls import reverse
from core.views import ListView, CreateView, UpdateView, DeleteView
from akademik.models import TahunAkademik, Kurikulum
from akademik.forms import TahunAkademikForm, KurikulumForm


class TahunAkademikListView(ListView):
    model = TahunAkademik
    title_page = 'Data Tahun Ajaran'


class TahunAkademikCreateView(CreateView):
    form_class = TahunAkademikForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data tahun ajaran'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data tahun ajaran", timer=5000)
        return reverse('akademik:list_tahun')


class TahunAkademikUpdateView(UpdateView):
    model = TahunAkademik
    form_class = TahunAkademikForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data tahun akademik'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data tahun ajaran", timer=5000)
        return reverse('akademik:list_tahun')


class TahunAkademikDeleteView(DeleteView):
    model = TahunAkademik

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data tahun ajaran", timer=5000)
        return reverse('akademik:list_tahun')


class KurikulumListView(ListView):
    model = Kurikulum
    title_page = 'Data Kurikulum'


class KurikulumCreateView(CreateView):
    form_class = KurikulumForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data kurikulum'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data kurikulum", timer=5000)
        return reverse('akademik:list_kurikulum')


class KurikulumUpdateView(UpdateView):
    model = Kurikulum
    form_class = KurikulumForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data kurikulum'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data kurikulum", timer=5000)
        return reverse('akademik:list_kurikulum')


class KurikulumDeleteView(DeleteView):
    model = Kurikulum

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data kurikulum", timer=5000)
        return reverse('akademik:list_kurikulum')
