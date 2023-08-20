from django.urls import path
from siswa import views

app_name = 'siswa'
urlpatterns = [
    path('list/', views.SiswaListView.as_view(), name='siswa_list'),
    path('create/', views.SiswaCreateView.as_view(), name='siswa_create'),
    path('edit/<uuid:id>/', views.SiswaUpdateView.as_view(), name='siswa_update'),
    path('detail/<uuid:id>/', views.SiswaDetailView.as_view(), name='siswa_detail'),
    path('delete/<uuid:id>/', views.SiswaDeleteView.as_view(), name='siswa_delete'),
]
