from django.urls import path
from akademik import views

app_name = 'akademik'
urlpatterns = [
    path('list/tahun/', views.TahunAkademikListView.as_view(), name='list_tahun'),
    path('create/tahun/', views.TahunAkademikCreateView.as_view(), name='create_tahun'),
    path('edit/tahun/<uuid:id>/', views.TahunAkademikUpdateView.as_view(), name='edit_tahun'),
    path('delete/tahun/<uuid:id>/', views.TahunAkademikDeleteView.as_view(), name='delete_tahun'),

    path('list/kurikulum/', views.KurikulumListView.as_view(), name='list_kurikulum'),
    path('create/kurikulum/', views.KurikulumCreateView.as_view(), name='create_kurikulum'),
    path('edit/kurikulum/<uuid:id>/', views.KurikulumUpdateView.as_view(), name='edit_kurikulum'),
    path('delete/kurikulum/<uuid:id>/', views.KurikulumDeleteView.as_view(), name='delete_kurikulum'),

    path('list/kolompokmapel/', views.KelompokMapelListView.as_view(), name='list_kelompokmapel'),
    path('create/kolompokmapel/', views.KelompokMapelCreateView.as_view(), name='create_kelompokmapel'),
    path('edit/kolompokmapel/<uuid:id>/', views.KelompokMapelUpdateView.as_view(), name='edit_kelompokmapel'),
    path('delete/kolompokmapel/<uuid:id>/', views.KelompokMapelDeleteView.as_view(), name='delete_kelompokmapel'),
]
