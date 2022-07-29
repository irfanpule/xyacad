from django.urls import path
from pegawai import views

app_name = 'pegawai'
urlpatterns = [
    path('list/', views.PegawaiListView.as_view(), name='list'),
    path('create/', views.PegawaiCreateView.as_view(), name='create'),
    path('edit/<uuid:id>/', views.PegawaiUpdateView.as_view(), name='edit'),
    path('detail/<uuid:id>/', views.PegawaiDetailView.as_view(), name='detail'),

    path('list/status/', views.StatusPegawaiListView.as_view(), name='list_status'),
    path('create/status/', views.StatusPegawaiCreateView.as_view(), name='create_status'),
    path('edit/status/<uuid:id>/', views.StatusPegawaiUpdateView.as_view(), name='edit_status'),
    path('delete/status/<uuid:id>/', views.StatusPegawaiDeleteView.as_view(), name='delete_status'),

    path('list/ptk/', views.JenisPTKListView.as_view(), name='list_ptk'),
    path('create/ptk/', views.JenisPTKCreateView.as_view(), name='create_ptk'),
    path('edit/ptk/<uuid:id>/', views.JenisPTKUpdateView.as_view(), name='edit_ptk'),
    path('delete/ptk/<uuid:id>/', views.JenisPTKDeleteView.as_view(), name='delete_ptk'),

    path('list/golongan/', views.GolonganListView.as_view(), name='list_golongan'),
    path('create/golongan/', views.GolonganCreateView.as_view(), name='create_golongan'),
    path('edit/golongan/<uuid:id>/', views.GolonganUpdateView.as_view(), name='edit_golongan'),
    path('delete/golongan/<uuid:id>/', views.GolonganDeleteView.as_view(), name='delete_golongan'),

    path('list/struktural/', views.JabatanStrukturalListView.as_view(), name='list_struktural'),
    path('create/struktural/', views.JabatanStrukturalCreateView.as_view(), name='create_struktural'),
    path('edit/struktural/<uuid:id>/', views.JabatanStrukturalUpdateView.as_view(), name='edit_struktural'),
    path('delete/struktural/<uuid:id>/', views.JabatanStrukturalDeleteView.as_view(), name='delete_struktural'),

    path('list/fungsional/', views.JabatanFungsionalListView.as_view(), name='list_fungsional'),
    path('create/fungsional/', views.JabatanFungsionalCreateView.as_view(), name='create_fungsional'),
    path('edit/fungsional/<uuid:id>/', views.JabatanFungsionalUpdateView.as_view(), name='edit_fungsional'),
    path('delete/fungsional/<uuid:id>/', views.JabatanFungsionalDeleteView.as_view(), name='delete_fungsional'),
]

