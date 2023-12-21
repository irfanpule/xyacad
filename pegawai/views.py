import datetime
import sweetify

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from core.views import ListBreadcrumbView, CreateBreadcrumbView, UpdateBreadcrumbView, BaseDeleteView, \
    DetailBreadcrumbView
from core.utils import Logger
from pegawai.models import StatusPegawai, JenisPTK, Golongan, JabatanStruktural, JabatanFungsional, Pegawai, Presensi
from pegawai.forms import (
    StatusPegawaiForm, JenisPTKForm, GolonganForm, JabatanStrukturalForm, JabatanFungsionalForm, PegawaiForm,
    PresensiHadirForm, PresensiSakitForm, PresensiIjinForm, PresensiCutiForm, PresensiClockInForm, PresensiClockOutForm,
    PresensiAktifForm
)


ACTIVE_MENU_MASTERPEGAWAI = 'masterpegawai'


class StatusPegawaiListView(ListBreadcrumbView):
    model = StatusPegawai
    title_page = 'Data Status Pegawai'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI


class StatusPegawaiCreateView(CreateBreadcrumbView):
    form_class = StatusPegawaiForm
    model = StatusPegawai
    template_name = 'pegawai/form_generic.html'
    title_page = 'Tambah data status pegawai'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data status pegawai", timer=5000)
        return reverse('pegawai:statuspegawai_list')


class StatusPegawaiUpdateView(UpdateBreadcrumbView):
    model = StatusPegawai
    form_class = StatusPegawaiForm
    template_name = 'pegawai/form_generic.html'
    title_page = 'Edit data status pegawai'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data status pegawai", timer=5000)
        return reverse('pegawai:statuspegawai_list')


class StatusPegawaiDetailView(DetailBreadcrumbView):
    model = StatusPegawai
    specific_sidebar_menu = 'pegawai/sidebar.html'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_title_page(self):
        return "Detail Status Pegawai"


class StatusPegawaiDeleteView(BaseDeleteView):
    model = StatusPegawai

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data status pegawai", timer=5000)
        return reverse('pegawai:statuspegawai_list')


class JenisPTKListView(ListBreadcrumbView):
    model = JenisPTK
    title_page = 'Data Jenis PTK'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI


class JenisPTKCreateView(CreateBreadcrumbView):
    form_class = JenisPTKForm
    model = JenisPTK
    template_name = 'pegawai/form_generic.html'
    title_page = 'Tambah data jenis PTK'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data Jenis PTK", timer=5000)
        return reverse('pegawai:jenisptk_list')


class JenisPTKUpdateView(UpdateBreadcrumbView):
    model = JenisPTK
    form_class = JenisPTKForm
    template_name = 'pegawai/form_generic.html'
    title_page = 'Edit data Jenis PTK'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data Jenis PTK", timer=5000)
        return reverse('pegawai:jenisptk_list')


class JenisPTKDetailView(DetailBreadcrumbView):
    model = JenisPTK
    specific_sidebar_menu = 'pegawai/sidebar.html'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_title_page(self):
        return "Detail Jenis PTK"


class JenisPTKDeleteView(BaseDeleteView):
    model = JenisPTK

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data Jenis PTK", timer=5000)
        return reverse('pegawai:jenisptk_list')


class GolonganListView(ListBreadcrumbView):
    model = Golongan
    title_page = 'Data Golongan'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI


class GolonganCreateView(CreateBreadcrumbView):
    form_class = GolonganForm
    model = Golongan
    template_name = 'pegawai/form_generic.html'
    title_page = 'Tambah data Golongan'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data golongan", timer=5000)
        return reverse('pegawai:golongan_list')


class GolonganUpdateView(UpdateBreadcrumbView):
    model = Golongan
    form_class = GolonganForm
    template_name = 'pegawai/form_generic.html'
    title_page = 'Edit data golongan'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data golongan", timer=5000)
        return reverse('pegawai:golongan_list')


class GolonganDetailView(DetailBreadcrumbView):
    model = Golongan
    specific_sidebar_menu = 'pegawai/sidebar.html'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_title_page(self):
        return "Detail Golongan"


class GolonganDeleteView(BaseDeleteView):
    model = Golongan

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data golongan", timer=5000)
        return reverse('pegawai:golongan_list')


class JabatanStrukturalListView(ListBreadcrumbView):
    model = JabatanStruktural
    title_page = 'Data Jabatan Struktural'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI


class JabatanStrukturalCreateView(CreateBreadcrumbView):
    form_class = JabatanStrukturalForm
    model = JabatanStruktural
    template_name = 'pegawai/form_generic.html'
    title_page = 'Tambah data jabatan struktural'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data jabatan struktural", timer=5000)
        return reverse('pegawai:jabatanstruktural_list')


class JabatanStrukturalUpdateView(UpdateBreadcrumbView):
    model = JabatanStruktural
    form_class = JabatanStrukturalForm
    template_name = 'pegawai/form_generic.html'
    title_page = 'Edit data jabatan struktural'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data jabatan struktural", timer=5000)
        return reverse('pegawai:jabatanstruktural_list')


class JabatanStrukturalDetailView(DetailBreadcrumbView):
    model = JabatanStruktural
    specific_sidebar_menu = 'pegawai/sidebar.html'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_title_page(self):
        return "Detail Jabatan Struktural"


class JabatanStrukturalDeleteView(BaseDeleteView):
    model = JabatanStruktural

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data jabatan struktural", timer=5000)
        return reverse('pegawai:jabatanstruktural_list')


class JabatanFungsionalListView(ListBreadcrumbView):
    model = JabatanFungsional
    title_page = 'Data Jabatan Fungsional'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI


class JabatanFungsionalCreateView(CreateBreadcrumbView):
    form_class = JabatanFungsionalForm
    model = JabatanFungsional
    template_name = 'pegawai/form_generic.html'
    title_page = 'Tambah data jabatan fungsional'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data jabatan fungsional", timer=5000)
        return reverse('pegawai:jabatanfungsional_list')


class JabatanFungsionalUpdateView(UpdateBreadcrumbView):
    model = JabatanFungsional
    form_class = JabatanFungsionalForm
    template_name = 'pegawai/form_generic.html'
    title_page = 'Edit data jabatan fungsional'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data jabatan fungsional", timer=5000)
        return reverse('pegawai:jabatanfungsional_list')


class JabatanFungsionalDetailView(DetailBreadcrumbView):
    model = JabatanFungsional
    specific_sidebar_menu = 'pegawai/sidebar.html'
    active_menu = ACTIVE_MENU_MASTERPEGAWAI

    def get_title_page(self):
        return "Detail Jabatan Fungsional"


class JabatanFungsionalDeleteView(BaseDeleteView):
    model = JabatanFungsional

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data jabatan fungsional", timer=5000)
        return reverse('pegawai:jabatanfungsional_list')


class PegawaiListView(ListBreadcrumbView):
    model = Pegawai
    title_page = 'Data Pegawai'
    active_menu = 'pegawai'


class PegawaiCreateView(CreateBreadcrumbView):
    form_class = PegawaiForm
    model = Pegawai
    template_name = 'pegawai/form_generic.html'
    title_page = 'Tambah data pegawai'
    btn_submit_name = 'Simpan'
    active_menu = 'pegawai'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data pegawai", timer=5000)
        return reverse('pegawai:pegawai_list')


class PegawaiUpdateView(UpdateBreadcrumbView):
    model = Pegawai
    form_class = PegawaiForm
    template_name = 'pegawai/form_generic.html'
    title_page = 'Tambah data pegawai'
    btn_submit_name = 'Simpan'
    active_menu = 'pegawai'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data pegawai", timer=5000)
        return reverse('pegawai:pegawai_list')


class PegawaiDetailView(DetailBreadcrumbView):
    model = Pegawai
    template_name = "pegawai/pegawai_detail.html"
    active_menu = 'pegawai'

    def get_title_page(self):
        return "Detail Pegawai"


class PegawaiIDCardView(DetailBreadcrumbView):
    model = Pegawai
    template_name = "pegawai/id_card.html"
    active_menu = 'pegawai'

    def get_title_page(self):
        return "Kartu Pagawai"


class PresensiPegawaiListView(ListBreadcrumbView):
    model = Presensi
    title_page = 'Presensi Pegawai'
    active_menu = 'pegawai'

    def get_context_data(self, **kwargs):
        context = super(PresensiPegawaiListView, self).get_context_data(**kwargs)
        context['presensi_aktif'] = self.request.session.get('presensi_aktif')
        return context


class PresensiDetailView(DetailBreadcrumbView):
    model = Presensi
    active_menu = 'pegawai'
    title_page = 'Presensi Pegawai'
    specific_sidebar_menu = 'pegawai/sidebar.html'


class PresensiDeleteView(BaseDeleteView):
    model = Presensi

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data presensi", timer=5000)
        return reverse('pegawai:presensi_list')


class PresensiHadirCreateView(CreateBreadcrumbView):
    model = Presensi
    title_page = 'Presensi Hadir'
    active_menu = 'pegawai'
    template_name = 'pegawai/form_generic.html'
    form_class = PresensiHadirForm
    btn_submit_name = "Simpan"

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data presensi hadir", timer=5000)
        return reverse('pegawai:presensi_list')


class PresensiSakitCreateView(CreateBreadcrumbView):
    model = Presensi
    title_page = 'Presensi Sakit'
    active_menu = 'pegawai'
    template_name = 'pegawai/form_generic.html'
    form_class = PresensiSakitForm
    btn_submit_name = "Simpan"

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data presensi sakit", timer=5000)
        return reverse('pegawai:presensi_list')


class PresensiIjinCreateView(CreateBreadcrumbView):
    model = Presensi
    title_page = 'Presensi Ijin'
    active_menu = 'pegawai'
    template_name = 'pegawai/form_generic.html'
    form_class = PresensiIjinForm
    btn_submit_name = "Simpan"

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data presensi ijin", timer=5000)
        return reverse('pegawai:presensi_list')


class PresensiCutiCreateView(CreateBreadcrumbView):
    model = Presensi
    title_page = 'Presensi Cuti'
    active_menu = 'pegawai'
    template_name = 'pegawai/form_generic.html'
    form_class = PresensiCutiForm
    btn_submit_name = "Simpan"

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data presensi cuti", timer=5000)
        return reverse('pegawai:presensi_list')


class PresensiUpdateView(UpdateBreadcrumbView):
    model = Presensi
    active_menu = 'pegawai'
    template_name = 'pegawai/form_generic.html'
    btn_submit_name = "Simpan"

    def get_success_url(self):
        sweetify.toast(self.request, 'Berhasil ubah data presensi', timer=5000)
        return reverse('pegawai:presensi_list')

    def get_form_class(self):
        obj = self.get_object()
        if obj.status == Presensi.STATUS.hadir:
            form = PresensiHadirForm
        elif obj.status == Presensi.STATUS.sakit:
            form = PresensiSakitForm
        elif obj.status == Presensi.STATUS.cuti:
            form = PresensiCutiForm
        else:
            form = PresensiIjinForm
        return form

    def get_title_page(self):
        obj = self.get_object()
        if obj.status == Presensi.STATUS.hadir:
            title = "Ubah Presensi Hadir"
        elif obj.status == Presensi.STATUS.sakit:
            title = "Ubah Presensi Sakit"
        elif obj.status == Presensi.STATUS.cuti:
            title = "Ubah Presensi Cuti"
        else:
            title = "Ubah Presensi Ijin"
        return title


def presensi_clockin(request):
    if not request.session.get('presensi_aktif'):
        return redirect("pegawai:presensi_aktifkan")

    form = PresensiClockInForm(request.POST or None)
    if form.is_valid():
        presensi = form.save()
        log = Logger()
        log.addition(request, presensi)
        sweetify.success(
            request,
            f"{presensi.pegawai.nama}",
            text=f"Berhasil Clock In {datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}",
            timer=5000,
        )
        return redirect(reverse("pegawai:presensi_clockin"))

    context = {
        'form': form,
        'title': "Presensi Clock In",
        'btn_submit_name': "Clock In"
    }
    return render(request, "pegawai/clockin.html", context)


def presensi_clockout(request):
    if not request.session.get('presensi_aktif'):
        return redirect("pegawai:presensi_aktifkan")

    form = PresensiClockOutForm(request.POST or None)
    if form.is_valid():
        presensi = form.save()
        log = Logger()
        log.change(request, presensi)
        sweetify.success(
            request,
            f"{presensi.pegawai.nama}",
            text=f"Berhasil Clock Out {datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}",
            timer=5000,
        )
        return redirect(reverse("pegawai:presensi_clockout"))

    context = {
        'form': form,
        'title': "Presensi Clock Out",
        'btn_submit_name': "Clock Out"
    }
    return render(request, "pegawai/clockout.html", context)


def presensi_aktifkan(request):
    form = PresensiAktifForm(request.POST or None)
    if form.is_valid():
        request.session["presensi_aktif"] = True
        sweetify.toast(request, "Kamu Berhasil Mengaktifkan halaman Presensi", timer=5000)
        return redirect("pegawai:presensi_clockin")

    context = {
        'form': form,
        'title': "Aktifkan Presensi",
        'btn_submit_name': "Aktifkan"
    }
    return render(request, "pegawai/aktifkan_presensi.html", context)


@staff_member_required
def presensi_nonaktifkan(request):
    if request.session.get("presensi_aktif"):
        request.session["presensi_aktif"] = None
        sweetify.toast(request, "Berhasil Menonaktifkan halaman Presensi", timer=5000)
        return redirect("pegawai:presensi_list")
    else:
        sweetify.toast(request, "Halaman Presensi Belum diaktifkan", timer=5000)
        return redirect("pegawai:presensi_list")
