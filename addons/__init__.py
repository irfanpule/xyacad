from django.conf import settings


def get_addons_list():
    addons_installed = []
    for app in settings.INSTALLED_ADDONS:
        _, app_name = app.split(".")
        import addons
        addons_installed.append({
            'app_name': app_name.title(),
            'index_url': eval(f'{app}.default_url'),
            'short_desc': eval(f'{app}.short_desc'),
            'icon': eval(f'{app}.icon'),
            'color': eval(f'{app}.color'),
        })
    return addons_installed
