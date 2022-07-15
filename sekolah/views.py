from django.views.generic.list import ListView
from core.mixin import ContextTitleMixin
from sekolah.models import Sekolah


class SekolahListView(ContextTitleMixin, ListView):
    model = Sekolah
    title_page = 'Data Sekolah'
    sub_title = 'Dapat menambahkan lebih dari 1 entitas sekolah'
