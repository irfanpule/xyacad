import sweetify
from django.urls import reverse
from core.views import ListView, CreateView, UpdateView, DeleteView, DetailView
from akademik.models import TahunAkademik, Kurikulum, KelompokMapel, Tingkat
from akademik.forms import TahunAkademikForm, KurikulumForm, KelompokMapelForm, TingkatForm


class TahunAkademikListView(ListView):
    model = TahunAkademik
    title_page = 'Data Tahun Ajaran'


class TahunAkademikCreateView(CreateView):
    form_class = TahunAkademikForm
    model = TahunAkademik
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data tahun ajaran'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data tahun ajaran", timer=5000)
        return reverse('akademik:tahunakademik_list')


class TahunAkademikUpdateView(UpdateView):
    model = TahunAkademik
    form_class = TahunAkademikForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data tahun akademik'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data tahun ajaran", timer=5000)
        return reverse('akademik:tahunakademik_list')


class TahunAkademikDetailView(DetailView):
    model = TahunAkademik

    def get_title_page(self):
        return "Detail Tahun Akademik"


class TahunAkademikDeleteView(DeleteView):
    model = TahunAkademik

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data tahun ajaran", timer=5000)
        return reverse('akademik:tahunakademik_list')


class KurikulumListView(ListView):
    model = Kurikulum
    title_page = 'Data Kurikulum'


class KurikulumCreateView(CreateView):
    form_class = KurikulumForm
    model = Kurikulum
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data kurikulum'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data kurikulum", timer=5000)
        return reverse('akademik:kurikulum_list')


class KurikulumUpdateView(UpdateView):
    model = Kurikulum
    form_class = KurikulumForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data kurikulum'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data kurikulum", timer=5000)
        return reverse('akademik:kurikulum_list')


class KurikulumDetailView(DetailView):
    model = Kurikulum

    def get_title_page(self):
        return "Detail Kurikulum"


class KurikulumDeleteView(DeleteView):
    model = Kurikulum

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data kurikulum", timer=5000)
        return reverse('akademik:kurikulum_list')


class KelompokMapelListView(ListView):
    model = KelompokMapel
    title_page = 'Data Kelompok Mate Pelajaran'


class KelompokMapelCreateView(CreateView):
    form_class = KelompokMapelForm
    model = KelompokMapel
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data kelompok mata pelajaran'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data kelompok mata pelajaran", timer=5000)
        return reverse('akademik:kelompokmapel_list')


class KelompokMapelUpdateView(UpdateView):
    model = KelompokMapel
    form_class = KelompokMapelForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data kurikulum'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data kelompok mata pelajaran", timer=5000)
        return reverse('akademik:kelompokmapel_list')


class KelompokMapelDetailView(DetailView):
    model = KelompokMapel

    def get_title_page(self):
        return "Detail Kelompok Mata Pelajaran"


class KelompokMapelDeleteView(DeleteView):
    model = KelompokMapel

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data kelompok mata pelajaran", timer=5000)
        return reverse('akademik:kelompokmapel_list')


class TingkatListView(ListView):
    model = Tingkat
    title_page = 'Data Tingkat'


class TingkatCreateView(CreateView):
    form_class = TingkatForm
    model = Tingkat
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data tingkat'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data tingkat", timer=5000)
        return reverse('akademik:tingkat_list')


class TingkatUpdateView(UpdateView):
    model = Tingkat
    form_class = TingkatForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data tingkat'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data tingkat", timer=5000)
        return reverse('akademik:tingkat_list')


class TingkatDetailView(DetailView):
    model = Tingkat

    def get_title_page(self):
        return "Detail Tingkat"


class TingkatDeleteView(DeleteView):
    model = Tingkat

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data tingkat", timer=5000)
        return reverse('akademik:tingkat_list')
