from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from core.mixin import ContextTitleMixin
from sekolah.models import Sekolah
from sekolah.forms import SekolahForm


class SekolahListView(ContextTitleMixin, ListView):
    model = Sekolah
    title_page = 'Data Sekolah'
    sub_title = 'Dapat menambahkan lebih dari 1 entitas sekolah'


class SekolahCreateView(ContextTitleMixin, CreateView):
    form_class = SekolahForm
    template_name = 'ui/two-column-form.html'
    title_page = 'Tambah data sekolah'
    sub_title = 'Jika pada Yayasan/Instansi terdapat SD, SMP, SMA dapat tambahkan disini'

    def get_success_url(self):
        return reverse('sekolah:list')
