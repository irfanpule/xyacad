from django.urls import path
from sekolah import views

app_name = 'sekolah'
urlpatterns = [
    path('list/', views.SekolahListView.as_view(), name='list'),
    path('create/', views.SekolahCreateView.as_view(), name='create'),
]
