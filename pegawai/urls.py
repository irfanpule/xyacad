from django.urls import path
from pegawai import views

app_name = 'pegawai'
urlpatterns = [
    path('list/status/', views.StatusPegawaiListView.as_view(), name='list_status'),
    path('create/status/', views.StatusPegawaiCreateView.as_view(), name='create_status'),
    path('edit/status/<uuid:id>/', views.StatusPegawaiUpdateView.as_view(), name='edit_status'),
    path('delete/status/<uuid:id>/', views.StatusPegawaiDeleteView.as_view(), name='delete_status'),
]

