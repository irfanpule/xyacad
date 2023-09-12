import importlib
from django.conf import settings


def get_addons_internal_list():
    addons_installed = []
    for app in settings.INSTALLED_ADDONS_INTERNAL:
        module = importlib.import_module(app)
        addons_installed.append({
            'app_name': app.title(),
            'index_url': module.default_url,
            'short_desc': module.short_desc,
            'icon': module.icon,
            'color': module.color,
        })
    return addons_installed
