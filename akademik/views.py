import sweetify
from django.urls import reverse

from core.mixin import FormFilterMixin
from core.views import (
    ListBreadcrumbView, CreateBreadcrumbView, UpdateBreadcrumbView, BaseDeleteView, DetailBreadcrumbView,
    BaseFormFilterView
)
from akademik.models import TahunAkademik, Kurikulum, KelompokMapel, Tingkat, MataPelajaran, Jadwal
from sekolah.models import Sekolah
from akademik.forms import (
    TahunAkademikForm, KurikulumForm, KelompokMapelForm, TingkatForm, MataPelajaranForm, JadwalForm,
    JadwalCreateFilterForm, JadwalShowWeeklyFilterForm
)


ACTIVE_MENU_MASTERAKDEMIK = 'masterakademik'


class TahunAkademikListView(ListBreadcrumbView):
    model = TahunAkademik
    title_page = 'Data Tahun Ajaran'
    active_menu = ACTIVE_MENU_MASTERAKDEMIK


class TahunAkademikCreateView(CreateBreadcrumbView):
    form_class = TahunAkademikForm
    model = TahunAkademik
    template_name = 'akademik/form_generic.html'
    title_page = 'Tambah data tahun ajaran'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERAKDEMIK

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data tahun ajaran", timer=5000)
        return reverse('akademik:tahunakademik_list')


class TahunAkademikUpdateView(UpdateBreadcrumbView):
    model = TahunAkademik
    form_class = TahunAkademikForm
    template_name = 'akademik/form_generic.html'
    title_page = 'Edit data tahun akademik'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERAKDEMIK

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data tahun ajaran", timer=5000)
        return reverse('akademik:tahunakademik_list')


class TahunAkademikDetailView(DetailBreadcrumbView):
    model = TahunAkademik
    specific_sidebar_menu = 'akademik/sidebar.html'
    active_menu = ACTIVE_MENU_MASTERAKDEMIK

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
    active_menu = ACTIVE_MENU_MASTERAKDEMIK

class KurikulumCreateView(CreateBreadcrumbView):
    form_class = KurikulumForm
    model = Kurikulum
    template_name = 'akademik/form_generic.html'
    title_page = 'Tambah data kurikulum'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERAKDEMIK

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data kurikulum", timer=5000)
        return reverse('akademik:kurikulum_list')


class KurikulumUpdateView(UpdateBreadcrumbView):
    model = Kurikulum
    form_class = KurikulumForm
    template_name = 'akademik/form_generic.html'
    title_page = 'Edit data kurikulum'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERAKDEMIK

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data kurikulum", timer=5000)
        return reverse('akademik:kurikulum_list')


class KurikulumDetailView(DetailBreadcrumbView):
    model = Kurikulum
    specific_sidebar_menu = 'akademik/sidebar.html'
    active_menu = ACTIVE_MENU_MASTERAKDEMIK

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
    active_menu = ACTIVE_MENU_MASTERAKDEMIK


class KelompokMapelCreateView(CreateBreadcrumbView):
    form_class = KelompokMapelForm
    model = KelompokMapel
    template_name = 'akademik/form_generic.html'
    title_page = 'Tambah data kelompok mata pelajaran'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERAKDEMIK

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data kelompok mata pelajaran", timer=5000)
        return reverse('akademik:kelompokmapel_list')


class KelompokMapelUpdateView(UpdateBreadcrumbView):
    model = KelompokMapel
    form_class = KelompokMapelForm
    template_name = 'akademik/form_generic.html'
    title_page = 'Edit data kurikulum'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERAKDEMIK

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data kelompok mata pelajaran", timer=5000)
        return reverse('akademik:kelompokmapel_list')


class KelompokMapelDetailView(DetailBreadcrumbView):
    model = KelompokMapel
    specific_sidebar_menu = 'akademik/sidebar.html'
    active_menu = ACTIVE_MENU_MASTERAKDEMIK

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
    active_menu = ACTIVE_MENU_MASTERAKDEMIK


class TingkatCreateView(CreateBreadcrumbView):
    form_class = TingkatForm
    model = Tingkat
    template_name = 'akademik/form_generic.html'
    title_page = 'Tambah data tingkat'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERAKDEMIK

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data tingkat", timer=5000)
        return reverse('akademik:tingkat_list')


class TingkatUpdateView(UpdateBreadcrumbView):
    model = Tingkat
    form_class = TingkatForm
    template_name = 'akademik/form_generic.html'
    title_page = 'Edit data tingkat'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERAKDEMIK

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data tingkat", timer=5000)
        return reverse('akademik:tingkat_list')


class TingkatDetailView(DetailBreadcrumbView):
    model = Tingkat
    specific_sidebar_menu = 'akademik/sidebar.html'
    active_menu = ACTIVE_MENU_MASTERAKDEMIK

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
    active_menu = 'akademik'


class MataPelajaranCreateView(CreateBreadcrumbView):
    form_class = MataPelajaranForm
    model = MataPelajaran
    template_name = 'akademik/form_generic.html'
    title_page = 'Tambah data mata pelajaran'
    btn_submit_name = 'Simpan'
    active_menu = 'akademik'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data mata pelajaran", timer=5000)
        return reverse('akademik:matapelajaran_list')


class MataPelajaranUpdateView(UpdateBreadcrumbView):
    model = MataPelajaran
    form_class = MataPelajaranForm
    template_name = 'akademik/form_generic.html'
    title_page = 'Edit data mata pelajaran'
    btn_submit_name = 'Simpan'
    active_menu = 'akademik'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data mata pelajaran", timer=5000)
        return reverse('akademik:matapelajaran_list')


class MataPelajaranDetailView(DetailBreadcrumbView):
    model = MataPelajaran
    specific_sidebar_menu = 'akademik/sidebar.html'
    active_menu = 'akademik'

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
    active_menu = 'akademik'


class JadwalCreateView(FormFilterMixin, CreateBreadcrumbView):
    form_class = JadwalForm
    form_filter = JadwalCreateFilterForm
    model = Jadwal
    template_name = 'akademik/form_jadwal.html'
    title_page = 'Tambah Jadwal'
    btn_submit_name = 'Simpan'
    active_menu = 'akademik'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context.get('sekolah') and context.get('tahun_ajaran'):
            context["additional_title"] = f"{context['sekolah']} {context['tahun_ajaran']}"
        return context

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        filter_fields = self.get_form_filter_fields()

        if filter_fields.get('sekolah'):
            kwargs = self.get_form_kwargs()
            filter_fields = self.get_form_filter_fields()
            kwargs['initial']['tahun_ajaran'] = filter_fields['tahun_ajaran']
            kwargs['initial']['sekolah'] = filter_fields['sekolah']
            return form_class(sekolah=filter_fields['sekolah'], **kwargs)
        else:
            return None

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan jadwal", timer=5000)
        return reverse('akademik:jadwal_list')


class JadwalUpdateView(UpdateBreadcrumbView):
    model = Jadwal
    form_class = JadwalForm
    template_name = 'akademik/form_generic.html'
    title_page = 'Edit jadwal'
    btn_submit_name = 'Simpan'
    sekolah: Sekolah = None
    active_menu = 'akademik'

    def dispatch(self, request, *args, **kwargs):
        jadwal = self.get_object()
        self.sekolah = jadwal.kelas.sekolah
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
    specific_sidebar_menu = 'akademik/sidebar.html'
    active_menu = 'akademik'

    def get_title_page(self):
        return "Detail Jadwal"


class JadwalDeleteView(BaseDeleteView):
    model = Jadwal

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus jadwal", timer=5000)
        return reverse('akademik:jadwal_list')


class JadwalShowWeekly(BaseFormFilterView):
    template_name = 'akademik/jadwal_show_weekly.html'
    form_filter = JadwalShowWeeklyFilterForm
    title_page = 'Lihat Jadwal Mingguan'
    active_menu = 'akademik'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context.get('sekolah') and context.get('tahun_ajaran') and context.get('kelas'):
            jadwal = Jadwal.objects.filter(
                sekolah=context['sekolah'],
                kelas=context['kelas'],
                tahun_ajaran=context['tahun_ajaran']
            ).order_by('jam_mulai')

            jadwal_mapping = {}
            for k, v in Jadwal.HARI.choices:
                jadwal_mapping[k] = []
                for j in jadwal:
                    if j.hari == k:
                        jadwal_mapping[k].append(j)

            context['jadwal'] = jadwal_mapping
        return context
