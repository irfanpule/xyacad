from django.urls import path
from sekolah import views

urlpatterns = [
    path('list/', views.SekolahListView.as_view(), name='list'),
]
