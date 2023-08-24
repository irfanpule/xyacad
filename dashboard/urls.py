from django.urls import path
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.home, name='home'),
    path('addons-apps', views.addons_app_list, name='addons_app_list'),
    path('form-general/', views.form_general, name='form_general'),
]
