from django.urls import path
from sekolah import views

app_name = 'sekolah'
urlpatterns = [
    path('list/', views.SekolahListView.as_view(), name='list'),
    path('create/', views.SekolahCreateView.as_view(), name='create'),
    path('edit/<uuid:id>/', views.SekolahUpdateView.as_view(), name='edit'),
    path('delete/<uuid:id>/', views.SekolahDeleteView.as_view(), name='delete'),
    path('detail/<uuid:id>/', views.SekolahDetailView.as_view(), name='detail'),

    path('list/gedung/', views.GedungListView.as_view(), name='list_gedung'),
    path('detail/gedung/<uuid:id>/', views.GedungDetailView.as_view(), name='detail_gedung'),
    path('edit/gedung/<uuid:id>/', views.GedungUpdateView.as_view(), name='edit_gedung'),
    path('create/gedung/', views.GedungCreateView.as_view(), name='create_gedung'),
    path('delete/gedung/<uuid:id>/', views.GedungDeleteView.as_view(), name='delete_gedung'),

    path('list/ruangan/', views.RuanganListView.as_view(), name='list_ruangan'),
    path('detail/ruangan/<uuid:id>/', views.RuanganDetailView.as_view(), name='detail_ruangan'),
    path('create/ruangan/', views.RuanganCreateView.as_view(), name='create_ruangan'),
    path('edit/ruangan/<uuid:id>/', views.RuanganUpdateView.as_view(), name='edit_ruangan'),
    path('delete/ruangan/<uuid:id>/', views.RuanganDeleteView.as_view(), name='delete_ruangan'),

    path('list/jurusan/', views.JurusanListView.as_view(), name='list_jurusan'),
    path('detail/jurusan/<uuid:id>/', views.JurusanDetailView.as_view(), name='detail_jurusan'),
    path('create/jurusan/', views.JurusanCreateView.as_view(), name='create_jurusan'),
    path('edit/jurusan/<uuid:id>/', views.JurusanUpdateView.as_view(), name='edit_jurusan'),
    path('delete/jurusan/<uuid:id>/', views.JurusanDeleteView.as_view(), name='delete_jurusan'),

    path('list/kelas/', views.KelasListView.as_view(), name='list_kelas'),
    path('detail/kelas/<uuid:id>/', views.KelasDetailView.as_view(), name='detail_kelas'),
    path('create/kelas/', views.KelasCreateView.as_view(), name='create_kelas'),
    path('edit/kelas/<uuid:id>/', views.KelasUpdateView.as_view(), name='edit_kelas'),
    path('delete/kelas/<uuid:id>/', views.KelasDeleteView.as_view(), name='delete_kelas'),
]
