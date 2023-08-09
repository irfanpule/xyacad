import sweetify
from django.urls import reverse
from core.views import (
    ListBreadcrumbView, CreateBreadcrumbView, UpdateBreadcrumbView, BaseDeleteView, DetailBreadcrumbView
)
from akademik.models import TahunAkademik, Kurikulum, KelompokMapel, Tingkat, MataPelajaran, Jadwal
from sekolah.models import Sekolah
from akademik.forms import (
    TahunAkademikForm, KurikulumForm, KelompokMapelForm, TingkatForm, MataPelajaranForm, JadwalForm, JadwalFilterForm
)


class TahunAkademikListView(ListBreadcrumbView):
    model = TahunAkademik
    title_page = 'Data Tahun Ajaran'


class TahunAkademikCreateView(CreateBreadcrumbView):
    form_class = TahunAkademikForm
    model = TahunAkademik
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data tahun ajaran'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data tahun ajaran", timer=5000)
        return reverse('akademik:tahunakademik_list')


class TahunAkademikUpdateView(UpdateBreadcrumbView):
    model = TahunAkademik
    form_class = TahunAkademikForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data tahun akademik'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data tahun ajaran", timer=5000)
        return reverse('akademik:tahunakademik_list')


class TahunAkademikDetailView(DetailBreadcrumbView):
    model = TahunAkademik

    def get_title_page(self):
        return "Detail Tahun Akademik"


class TahunAkademikDeleteView(BaseDeleteView):
    model = TahunAkademik

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data tahun ajaran", timer=5000)
        return reverse('akademik:tahunakademik_list')


class KurikulumListView(ListBreadcrumbView):
    model = Kurikulum
    title_page = 'Data Kurikulum'


class KurikulumCreateView(CreateBreadcrumbView):
    form_class = KurikulumForm
    model = Kurikulum
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data kurikulum'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data kurikulum", timer=5000)
        return reverse('akademik:kurikulum_list')


class KurikulumUpdateView(UpdateBreadcrumbView):
    model = Kurikulum
    form_class = KurikulumForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data kurikulum'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data kurikulum", timer=5000)
        return reverse('akademik:kurikulum_list')


class KurikulumDetailView(DetailBreadcrumbView):
    model = Kurikulum

    def get_title_page(self):
        return "Detail Kurikulum"


class KurikulumDeleteView(BaseDeleteView):
    model = Kurikulum

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data kurikulum", timer=5000)
        return reverse('akademik:kurikulum_list')


class KelompokMapelListView(ListBreadcrumbView):
    model = KelompokMapel
    title_page = 'Data Kelompok Mate Pelajaran'


class KelompokMapelCreateView(CreateBreadcrumbView):
    form_class = KelompokMapelForm
    model = KelompokMapel
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data kelompok mata pelajaran'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data kelompok mata pelajaran", timer=5000)
        return reverse('akademik:kelompokmapel_list')


class KelompokMapelUpdateView(UpdateBreadcrumbView):
    model = KelompokMapel
    form_class = KelompokMapelForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data kurikulum'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data kelompok mata pelajaran", timer=5000)
        return reverse('akademik:kelompokmapel_list')


class KelompokMapelDetailView(DetailBreadcrumbView):
    model = KelompokMapel

    def get_title_page(self):
        return "Detail Kelompok Mata Pelajaran"


class KelompokMapelDeleteView(BaseDeleteView):
    model = KelompokMapel

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data kelompok mata pelajaran", timer=5000)
        return reverse('akademik:kelompokmapel_list')


class TingkatListView(ListBreadcrumbView):
    model = Tingkat
    title_page = 'Data Tingkat'


class TingkatCreateView(CreateBreadcrumbView):
    form_class = TingkatForm
    model = Tingkat
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data tingkat'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data tingkat", timer=5000)
        return reverse('akademik:tingkat_list')


class TingkatUpdateView(UpdateBreadcrumbView):
    model = Tingkat
    form_class = TingkatForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data tingkat'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data tingkat", timer=5000)
        return reverse('akademik:tingkat_list')


class TingkatDetailView(DetailBreadcrumbView):
    model = Tingkat

    def get_title_page(self):
        return "Detail Tingkat"


class TingkatDeleteView(BaseDeleteView):
    model = Tingkat

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data tingkat", timer=5000)
        return reverse('akademik:tingkat_list')


class MataPelajaranListView(ListBreadcrumbView):
    model = MataPelajaran
    title_page = 'Data Mata Pelajaran'


class MataPelajaranCreateView(CreateBreadcrumbView):
    form_class = MataPelajaranForm
    model = MataPelajaran
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data mata pelajaran'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data mata pelajaran", timer=5000)
        return reverse('akademik:matapelajaran_list')


class MataPelajaranUpdateView(UpdateBreadcrumbView):
    model = MataPelajaran
    form_class = MataPelajaranForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit data mata pelajaran'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data mata pelajaran", timer=5000)
        return reverse('akademik:matapelajaran_list')


class MataPelajaranDetailView(DetailBreadcrumbView):
    model = MataPelajaran

    def get_title_page(self):
        return "Detail Mata Pelajaran"


class MataPelajaranDeleteView(BaseDeleteView):
    model = MataPelajaran

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data mata pelajaran", timer=5000)
        return reverse('akademik:matapelajaran_list')


class JadwalListView(ListBreadcrumbView):
    model = Jadwal
    title_page = 'Data Jadwal'


class JadwalCreateView(CreateBreadcrumbView):
    form_class = JadwalForm
    model = Jadwal
    template_name = 'akademik/form_jadwal.html'
    title_page = 'Tambah Jadwal'
    btn_submit_name = 'Simpan'
    sekolah: Sekolah = None
    tahun_ajaran = None

    def dispatch(self, request, *args, **kwargs):
        sekolah = request.GET.get('sekolah', None)
        tahun_ajaran = request.GET.get('tahun_ajaran', None)
        if sekolah:
            self.sekolah = Sekolah.objects.get(id=sekolah)
        if tahun_ajaran:
            self.tahun_ajaran = TahunAkademik.objects.get(id=tahun_ajaran)

        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        if self.sekolah:
            kwargs = self.get_form_kwargs()
            kwargs['initial']['tahun_ajaran'] = self.tahun_ajaran
            return form_class(sekolah=self.sekolah, **kwargs)
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = JadwalFilterForm()
        if self.sekolah and self.tahun_ajaran:
            context["additional_title"] = f"{self.sekolah.nama} {self.tahun_ajaran.nama}"
        context['sekolah'] = self.sekolah
        return context

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan jadwal", timer=5000)
        return reverse('akademik:jadwal_list')


class JadwalUpdateView(UpdateBreadcrumbView):
    model = Jadwal
    form_class = JadwalForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Edit jadwal'
    btn_submit_name = 'Simpan'
    sekolah: Sekolah = None

    def dispatch(self, request, *args, **kwargs):
        jadwal = self.get_object()
        self.sekolah = jadwal.kelas.ruangan.gedung.sekolah
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        if self.sekolah:
            return form_class(sekolah=self.sekolah, **self.get_form_kwargs())
        else:
            return None

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah jadwal", timer=5000)
        return reverse('akademik:jadwal_list')


class JadwalDetailView(DetailBreadcrumbView):
    model = Jadwal

    def get_title_page(self):
        return "Detail Jadwal"


class JadwalDeleteView(BaseDeleteView):
    model = Jadwal

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus jadwal", timer=5000)
        return reverse('akademik:jadwal_list')
