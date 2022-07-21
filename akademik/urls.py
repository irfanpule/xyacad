from django.urls import path
from akademik import views

app_name = 'akademik'
urlpatterns = [
    path('list/tahun/', views.TahunAkademikListView.as_view(), name='list_tahun'),
    path('create/tahun/', views.TahunAkademikCreateView.as_view(), name='create_tahun'),
    path('edit/tahun/<uuid:id>/', views.TahunAkademikUpdateView.as_view(), name='edit_tahun'),
    path('delete/tahun/<uuid:id>/', views.TahunAkademikDeleteView.as_view(), name='delete_tahun'),
]
