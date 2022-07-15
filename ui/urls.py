from django.urls import path
from ui import views

app_name = 'ui'
urlpatterns = [
    path('', views.home, name='home'),
    path('form-general/', views.form_general, name='form_general'),
]
