from django.conf import settings
from django.urls import path, include


# generate urlpatterns from addons registered
urlpatterns = []
for app in settings.INSTALLED_ADDONS:
    _, app_name = app.split(".")
    urlpatterns.append(
        path(f'{app_name}/', include(f'addons.{app_name}.urls')),
    )
