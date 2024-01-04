import sweetify
from django.shortcuts import redirect
from django.urls import reverse

from core.mixin import FormFilterMixin
from core.views import (
    ListBreadcrumbView, CreateBreadcrumbView, UpdateBreadcrumbView, BaseDeleteView, DetailBreadcrumbView
)
from core.utils import Logger
from siswa.models import Siswa, SiswaKelas, PresensiSiswa, PresensiSiswaHarian
from siswa.forms import (
    SiswaForm, SiswaKelasForm, SiswaKelasCreateFilterForm, PresensiSiswaForm, PresensiSiswaUpdateForm
)
from akademik.models import Jadwal


ACTIVE_MENU_SISWA = 'siswa'
ACTIVE_MENU_SISWAKELAS = 'siswakelas'
ACTIVE_MENU_PRESENSISISWA = 'presensisiswa'


class SiswaListView(ListBreadcrumbView):
    model = Siswa
    title_page = 'Data Siswa'
    active_menu = ACTIVE_MENU_SISWA


class SiswaCreateView(CreateBreadcrumbView):
    form_class = SiswaForm
    model = Siswa
    template_name = 'siswa/form_generic.html'
    title_page = 'Tambah data siswa'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_SISWA

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data siswa", timer=5000)
        return reverse('siswa:siswa_list')


class SiswaUpdateView(UpdateBreadcrumbView):
    model = Siswa
    form_class = SiswaForm
    template_name = 'siswa/form_generic.html'
    title_page = 'Tambah data siswa'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_SISWA

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data siswa", timer=5000)
        return reverse('siswa:siswa_list')


class SiswaDetailView(DetailBreadcrumbView):
    model = Siswa
    template_name = "siswa/siswa_detail.html"
    active_menu = ACTIVE_MENU_SISWA

    def get_title_page(self):
        return "Detail Siswa"


class SiswaDeleteView(BaseDeleteView):
    model = Siswa

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus siswa", timer=5000)
        return reverse('siswa:siswa_list')


class SiswaKelasListView(ListBreadcrumbView):
    model = SiswaKelas
    title_page = 'Data Siswa Kelas'
    active_menu = ACTIVE_MENU_SISWAKELAS


class SiswaKelasCreateView(FormFilterMixin, CreateBreadcrumbView):
    form_class = SiswaKelasForm
    form_filter = SiswaKelasCreateFilterForm
    model = SiswaKelas
    template_name = 'siswa/form_siswakelas.html'
    title_page = 'Tambah data siswa kelas'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_SISWAKELAS

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
            return form_class(sekolah=filter_fields['sekolah'], **kwargs)
        else:
            return None

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data siswa kelas", timer=5000)
        return reverse('siswa:siswakelas_list')


class SiswaKelasUpdateView(UpdateBreadcrumbView):
    model = SiswaKelas
    form_class = SiswaKelasForm
    template_name = 'siswa/form_generic.html'
    title_page = 'Tambah data siswa kelas'
    btn_submit_name = 'Simpan'
    active_menu = ACTIVE_MENU_SISWAKELAS

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data siswa", timer=5000)
        return reverse('siswa:siswakelas_list')


class SiswaKelasDetailView(DetailBreadcrumbView):
    model = SiswaKelas
    active_menu = ACTIVE_MENU_SISWAKELAS
    specific_sidebar_menu = 'siswa/sidebar.html'

    def get_title_page(self):
        return "Detail Siswa Kelas"


class SiswaKelasDeleteView(BaseDeleteView):
    model = SiswaKelas

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus siswa kelas", timer=5000)
        return reverse('siswa:siswakelas_list')


class SiswaIDCardView(DetailBreadcrumbView):
    model = Siswa
    template_name = "siswa/id_card.html"
    active_menu = ACTIVE_MENU_SISWA

    def get_title_page(self):
        return "Kartu Pelajar"


class PresensiSiswaCreateView(DetailBreadcrumbView):
    model = Jadwal
    active_menu = ACTIVE_MENU_PRESENSISISWA
    template_name = "siswa/presensi_siswa.html"

    def post(self, request, *args, **kwargs):
        jadwal = self.get_object()
        forms = [
            PresensiSiswaForm(dict(siswa_kelas=sk, status=status))
            for sk, status in zip(
                request.POST.getlist("siswa_kelas"),
                request.POST.getlist("status")
            )
        ]
        if all(forms[i].is_valid() for i in range(len(forms))):
            presensi_harian = PresensiSiswaHarian.objects.create(
                jadwal=jadwal, user=request.user, ket=request.POST.get("ket"))

            for form in forms:
                presensi = form.save(commit=False)
                presensi.jadwal = jadwal
                presensi.save()

                presensi_harian.presensi_siswa.add(presensi)
                presensi_harian.save()
                log = Logger()
                log.addition(request, presensi_harian)

            sweetify.toast(self.request, "Berhasil Tambah Data Presensi")
            return redirect("siswa:siswa_presensi", id=jadwal.id)
        else:
            sweetify.toast(self.request, "Terjadi kesalahan", icon="warning")
            return redirect("siswa:siswa_presensi", id=jadwal.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jadwal = self.get_object()
        siswa_kelas = SiswaKelas.objects.filter(kelas=jadwal.kelas, tahun_ajaran=jadwal.tahun_ajaran)
        context['jadwal'] = jadwal
        forms = []
        for sk in siswa_kelas:
            forms.append(
                PresensiSiswaForm(initial={'siswa_kelas': sk})
            )
        context['forms'] = forms
        return context

    def get_title_page(self):
        return "Presensi Siswa"


class PresensiSiswaUpdateView(DetailBreadcrumbView):
    model = PresensiSiswaHarian
    active_menu = ACTIVE_MENU_PRESENSISISWA
    template_name = "siswa/presensi_siswa.html"

    def post(self, request, *args, **kwargs):
        presensi_harian = self.get_object()
        jadwal = presensi_harian.jadwal
        forms = [
            PresensiSiswaUpdateForm(
                dict(siswa_kelas=sk, status=status, id=id),
                instance=PresensiSiswa.objects.get(id=id)
            )
            for sk, status, id in zip(
                request.POST.getlist("siswa_kelas"),
                request.POST.getlist("status"),
                request.POST.getlist("id")
            )
        ]
        if all(forms[i].is_valid() for i in range(len(forms))):

            for form in forms:
                presensi = form.save(commit=False)
                presensi.jadwal = jadwal
                presensi.save()

            presensi_harian.ket = request.POST.get("ket")
            presensi_harian.user = request.user
            presensi_harian.save()
            log = Logger()
            log.change(request, presensi_harian)

            sweetify.toast(self.request, "Berhasil Ubah Data Presensi")
            return redirect("siswa:presensisiswaharian_detail", id=presensi_harian.id)
        else:
            sweetify.toast(self.request, "Terjadi kesalahan", icon="warning")
            return redirect("siswa:presensisiswaharian_update", id=presensi_harian.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        presensi_harian = self.get_object()
        jadwal = presensi_harian.jadwal
        context['jadwal'] = jadwal
        forms = []
        for ps in presensi_harian.presensi_siswa.all():
            forms.append(
                PresensiSiswaUpdateForm(instance=ps, initial={'id': ps.id})
            )
        context['forms'] = forms
        context['ket'] = presensi_harian.ket
        return context

    def get_title_page(self):
        return "Ubah Presensi Siswa"


class PresensiSiswaHarianListView(ListBreadcrumbView):
    model = PresensiSiswaHarian
    title_page = 'Data Presensi Siswa Harian'
    active_menu = ACTIVE_MENU_PRESENSISISWA


class PresensiSiswaHarianDetailView(DetailBreadcrumbView):
    model = PresensiSiswaHarian
    active_menu = ACTIVE_MENU_PRESENSISISWA
    template_name = 'siswa/presensi_siswa_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jadwal'] = self.get_object().jadwal
        return context

    def get_title_page(self):
        return "Detail Presensi Siswa"
