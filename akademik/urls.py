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
]
