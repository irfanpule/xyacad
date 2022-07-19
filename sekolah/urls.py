from django.urls import path
from sekolah import views

app_name = 'sekolah'
urlpatterns = [
    path('list/', views.SekolahListView.as_view(), name='list'),
    path('create/', views.SekolahCreateView.as_view(), name='create'),
    path('edit/<uuid:id>/', views.SekolahUpdateView.as_view(), name='edit'),
    path('delete/<uuid:id>/', views.SekolahDeleteView.as_view(), name='delete'),
    path('detail/<uuid:id>/', views.SekolahDetailView.as_view(), name='detail'),
]
