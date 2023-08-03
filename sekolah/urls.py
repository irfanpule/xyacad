from django.urls import path
from sekolah import views

app_name = 'sekolah'
urlpatterns = [
    path('list/', views.SekolahListView.as_view(), name='sekolah_list'),
    path('create/', views.SekolahCreateView.as_view(), name='sekolah_create'),
    path('edit/<uuid:id>/', views.SekolahUpdateView.as_view(), name='sekolah_update'),
    path('delete/<uuid:id>/', views.SekolahDeleteView.as_view(), name='sekolah_delete'),
    path('detail/<uuid:id>/', views.SekolahDetailView.as_view(), name='sekolah_detail'),

    path('gedung/list/', views.GedungListView.as_view(), name='gedung_list'),
    path('gedung/create/', views.GedungCreateView.as_view(), name='gedung_create'),
    path('gedung/edit/<uuid:id>/', views.GedungUpdateView.as_view(), name='gedung_update'),
    path('gedung/detail/<uuid:id>/', views.GedungDetailView.as_view(), name='gedung_detail'),
    path('gedung/delete/<uuid:id>/', views.GedungDeleteView.as_view(), name='gedung_delete'),

    path('ruangan/list/', views.RuanganListView.as_view(), name='ruangan_list'),
    path('ruangan/create/', views.RuanganCreateView.as_view(), name='ruangan_create'),
    path('ruangan/edit/<uuid:id>/', views.RuanganUpdateView.as_view(), name='ruangan_update'),
    path('ruangan/detail/<uuid:id>/', views.RuanganDetailView.as_view(), name='ruangan_detail'),
    path('ruangan/delete/<uuid:id>/', views.RuanganDeleteView.as_view(), name='ruangan_delete'),

    path('jurusan/list/', views.JurusanListView.as_view(), name='jurusan_list'),
    path('jurusan/create/', views.JurusanCreateView.as_view(), name='jurusan_create'),
    path('jurusan/edit/<uuid:id>/', views.JurusanUpdateView.as_view(), name='jurusan_update'),
    path('jurusan/detail/<uuid:id>/', views.JurusanDetailView.as_view(), name='jurusan_detail'),
    path('jurusan/delete/<uuid:id>/', views.JurusanDeleteView.as_view(), name='jurusan_delete'),

    path('kelas/list/', views.KelasListView.as_view(), name='kelas_list'),
    path('kelas/create/', views.KelasCreateView.as_view(), name='kelas_create'),
    path('kelas/edit/<uuid:id>/', views.KelasUpdateView.as_view(), name='kelas_update'),
    path('kelas/detail/<uuid:id>/', views.KelasDetailView.as_view(), name='kelas_detail'),
    path('kelas/delete/<uuid:id>/', views.KelasDeleteView.as_view(), name='kelas_delete'),
]
