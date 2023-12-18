from django.urls import path
from pegawai import views

app_name = 'pegawai'
urlpatterns = [
    path('list/', views.PegawaiListView.as_view(), name='pegawai_list'),
    path('create/', views.PegawaiCreateView.as_view(), name='pegawai_create'),
    path('edit/<uuid:id>/', views.PegawaiUpdateView.as_view(), name='pegawai_update'),
    path('detail/<uuid:id>/', views.PegawaiDetailView.as_view(), name='pegawai_detail'),
    path('id-card/<uuid:id>/', views.PegawaiIDCardView.as_view(), name='pegawai_id_card'),

    path('status/list/', views.StatusPegawaiListView.as_view(), name='statuspegawai_list'),
    path('status/create/', views.StatusPegawaiCreateView.as_view(), name='statuspegawai_create'),
    path('status/edit/<uuid:id>/', views.StatusPegawaiUpdateView.as_view(), name='statuspegawai_update'),
    path('status/detail/<uuid:id>/', views.StatusPegawaiDetailView.as_view(), name='statuspegawai_detail'),
    path('status/delete/<uuid:id>/', views.StatusPegawaiDeleteView.as_view(), name='statuspegawai_delete'),

    path('ptk/list/', views.JenisPTKListView.as_view(), name='jenisptk_list'),
    path('ptk/create/', views.JenisPTKCreateView.as_view(), name='jenisptk_create'),
    path('ptk/edit/<uuid:id>/', views.JenisPTKUpdateView.as_view(), name='jenisptk_update'),
    path('ptk/detail/<uuid:id>/', views.JenisPTKDetailView.as_view(), name='jenisptk_detail'),
    path('ptk/delete/<uuid:id>/', views.JenisPTKDeleteView.as_view(), name='jenisptk_delete'),

    path('golongan/list/', views.GolonganListView.as_view(), name='golongan_list'),
    path('golongan/create/', views.GolonganCreateView.as_view(), name='golongan_create'),
    path('golongan/edit/<uuid:id>/', views.GolonganUpdateView.as_view(), name='golongan_update'),
    path('golongan/detail/<uuid:id>/', views.GolonganDetailView.as_view(), name='golongan_detail'),
    path('golongan/delete/<uuid:id>/', views.GolonganDeleteView.as_view(), name='golongan_delete'),

    path('struktural/list/', views.JabatanStrukturalListView.as_view(), name='jabatanstruktural_list'),
    path('struktural/create/', views.JabatanStrukturalCreateView.as_view(), name='jabatanstruktural_create'),
    path('struktural/edit/<uuid:id>/', views.JabatanStrukturalUpdateView.as_view(), name='jabatanstruktural_update'),
    path('struktural/detail/<uuid:id>/', views.JabatanStrukturalDetailView.as_view(), name='jabatanstruktural_detail'),
    path('struktural/delete/<uuid:id>/', views.JabatanStrukturalDeleteView.as_view(), name='jabatanstruktural_delete'),

    path('fungsional/list/', views.JabatanFungsionalListView.as_view(), name='jabatanfungsional_list'),
    path('fungsional/create/', views.JabatanFungsionalCreateView.as_view(), name='jabatanfungsional_create'),
    path('fungsional/edit/<uuid:id>/', views.JabatanFungsionalUpdateView.as_view(), name='jabatanfungsional_update'),
    path('fungsional/detail/<uuid:id>/', views.JabatanFungsionalDetailView.as_view(), name='jabatanfungsional_detail'),
    path('fungsional/delete/<uuid:id>/', views.JabatanFungsionalDeleteView.as_view(), name='jabatanfungsional_delete'),

    path('presensi/list/', views.PresensiPegawaiListView.as_view(), name='presensi_list'),
    path('presensi/detail/<uuid:id>/', views.PresensiDetailView.as_view(), name='presensi_detail'),
    path('presensi/edit/<uuid:id>/', views.PresensiUpdateView.as_view(), name='presensi_update'),
    path('presensi/delete/<uuid:id>/', views.PresensiDeleteView.as_view(), name='presensi_delete'),
    path('presensi/create/hadir/', views.PresensiHadirCreateView.as_view(), name='presensi_create'),
    path('presensi/create/sakit/', views.PresensiSakitCreateView.as_view(), name='presensi_sakit_create'),
    path('presensi/create/ijin/', views.PresensiIjinCreateView.as_view(), name='presensi_ijin_create'),
    path('presensi/create/cuti/', views.PresensiCutiCreateView.as_view(), name='presensi_cuti_create'),

    path('presensi/clockin/', views.presensi_clockin, name='presensi_clockin'),
    path('presensi/clockout/', views.presensi_clockout, name='presensi_clockout'),

]

