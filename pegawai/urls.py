from django.urls import path
from pegawai import views

app_name = 'pegawai'
urlpatterns = [
    path('list/status/', views.StatusPegawaiListView.as_view(), name='list_status'),
    path('create/status/', views.StatusPegawaiCreateView.as_view(), name='create_status'),
    path('edit/status/<uuid:id>/', views.StatusPegawaiUpdateView.as_view(), name='edit_status'),
    path('delete/status/<uuid:id>/', views.StatusPegawaiDeleteView.as_view(), name='delete_status'),

    path('list/ptk/', views.JenisPTKListView.as_view(), name='list_ptk'),
    path('create/ptk/', views.JenisPTKCreateView.as_view(), name='create_ptk'),
    path('edit/ptk/<uuid:id>/', views.JenisPTKUpdateView.as_view(), name='edit_ptk'),
    path('delete/ptk/<uuid:id>/', views.JenisPTKDeleteView.as_view(), name='delete_ptk'),
]

