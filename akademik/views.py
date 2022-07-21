import sweetify
from django.urls import reverse
from core.views import ListView, CreateView, UpdateView, DeleteView
from akademik.models import TahunAkademik
from akademik.forms import TahunAkademikForm


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
