from django.urls import path
from akademik import views

app_name = 'akademik'
urlpatterns = [
    path('tahun/list/', views.TahunAkademikListView.as_view(), name='tahunakademik_list'),
    path('tahun/create/', views.TahunAkademikCreateView.as_view(), name='tahunakademik_create'),
    path('tahun/edit/<uuid:id>/', views.TahunAkademikUpdateView.as_view(), name='tahunakademik_update'),
    path('tahun/detail/<uuid:id>/', views.TahunAkademikDetailView.as_view(), name='tahunakademik_detail'),
    path('tahun/delete/<uuid:id>/', views.TahunAkademikDeleteView.as_view(), name='tahunakademik_delete'),

    path('kurikulum/list/', views.KurikulumListView.as_view(), name='kurikulum_list'),
    path('kurikulum/create/', views.KurikulumCreateView.as_view(), name='kurikulum_create'),
    path('kurikulum/edit/<uuid:id>/', views.KurikulumUpdateView.as_view(), name='kurikulum_update'),
    path('kurikulum/detail/<uuid:id>/', views.KurikulumDetailView.as_view(), name='kurikulum_detail'),
    path('kurikulum/delete/<uuid:id>/', views.KurikulumDeleteView.as_view(), name='kurikulum_delete'),

    path('kolompokmapel/list/', views.KelompokMapelListView.as_view(), name='kelompokmapel_list'),
    path('kolompokmapel/create/', views.KelompokMapelCreateView.as_view(), name='kelompokmapel_create'),
    path('kolompokmapel/edit/<uuid:id>/', views.KelompokMapelUpdateView.as_view(), name='kelompokmapel_update'),
    path('kolompokmapel/detail/<uuid:id>/', views.KelompokMapelDetailView.as_view(), name='kelompokmapel_detail'),
    path('kolompokmapel/delete/<uuid:id>/', views.KelompokMapelDeleteView.as_view(), name='kelompokmapel_delete'),

    path('tingkat/list/', views.TingkatListView.as_view(), name='tingkat_list'),
    path('tingkat/create/', views.TingkatCreateView.as_view(), name='tingkat_create'),
    path('tingkat/edit/<uuid:id>/', views.TingkatUpdateView.as_view(), name='tingkat_update'),
    path('tingkat/detail/<uuid:id>/', views.TingkatDetailView.as_view(), name='tingkat_detail'),
    path('tingkat/delete/<uuid:id>/', views.TingkatDeleteView.as_view(), name='tingkat_delete'),

    path('matapelajaran/list/', views.MataPelajaranListView.as_view(), name='matapelajaran_list'),
    path('matapelajaran/create/', views.MataPelajaranCreateView.as_view(), name='matapelajaran_create'),
    path('matapelajaran/edit/<uuid:id>/', views.MataPelajaranUpdateView.as_view(), name='matapelajaran_update'),
    path('matapelajaran/detail/<uuid:id>/', views.MataPelajaranDetailView.as_view(), name='matapelajaran_detail'),
    path('matapelajaran/delete/<uuid:id>/', views.MataPelajaranDeleteView.as_view(), name='matapelajaran_delete'),
]
