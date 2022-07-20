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
]

