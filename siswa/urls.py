from django.urls import path
from siswa import views

app_name = 'siswa'
urlpatterns = [
    path('list/', views.SiswaListView.as_view(), name='siswa_list'),
    path('create/', views.SiswaCreateView.as_view(), name='siswa_create'),
    path('edit/<uuid:id>/', views.SiswaUpdateView.as_view(), name='siswa_update'),
    path('detail/<uuid:id>/', views.SiswaDetailView.as_view(), name='siswa_detail'),
    path('delete/<uuid:id>/', views.SiswaDeleteView.as_view(), name='siswa_delete'),
    path('kartu-pelajar/<uuid:id>/', views.SiswaIDCardView.as_view(), name='siswa_id_card'),

    path('kelas/list/', views.SiswaKelasListView.as_view(), name='siswakelas_list'),
    path('kelas/create/', views.SiswaKelasCreateView.as_view(), name='siswakelas_create'),
    path('kelas/edit/<uuid:id>/', views.SiswaKelasUpdateView.as_view(), name='siswakelas_update'),
    path('kelas/detail/<uuid:id>/', views.SiswaKelasDetailView.as_view(), name='siswakelas_detail'),
    path('kelas/delete/<uuid:id>/', views.SiswaKelasDeleteView.as_view(), name='siswakelas_delete'),
]
