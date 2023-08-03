from django.urls import path
from akademik import views

app_name = 'akademik'
urlpatterns = [
    path('tahun/list/', views.TahunAkademikListView.as_view(), name='tahunakademik_list'),
    path('tahun/create/', views.TahunAkademikCreateView.as_view(), name='tahunakademik_create'),
    path('tahun/edit/<uuid:id>/', views.TahunAkademikUpdateView.as_view(), name='tahunakademik_update'),
    path('tahun/delete/<uuid:id>/', views.TahunAkademikDeleteView.as_view(), name='tahunakademik_delete'),

    path('kurikulum/list/', views.KurikulumListView.as_view(), name='kurikulum_list'),
    path('kurikulum/create/', views.KurikulumCreateView.as_view(), name='kurikulum_create'),
    path('kurikulum/edit/<uuid:id>/', views.KurikulumUpdateView.as_view(), name='kurikulum_update'),
    path('kurikulum/delete/<uuid:id>/', views.KurikulumDeleteView.as_view(), name='kurikulum_delete'),

    path('kolompokmapel/list/', views.KelompokMapelListView.as_view(), name='list_kelompokmapel'),
    path('kolompokmapel/create/', views.KelompokMapelCreateView.as_view(), name='create_kelompokmapel'),
    path('kolompokmapel/edit/<uuid:id>/', views.KelompokMapelUpdateView.as_view(), name='edit_kelompokmapel'),
    path('kolompokmapel/delete/<uuid:id>/', views.KelompokMapelDeleteView.as_view(), name='delete_kelompokmapel'),
]
