import sweetify
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from addons import get_addons_list


@login_required
def home(request):
    return render(request, 'dashboard/home.html')


@login_required
def addons_app_list(request):
    context = {
        'addons_list': get_addons_list()
    }
    return render(request, 'dashboard/addosn_app_list.html', context)


def form_general(request):
    return render(request, 'dashboard/two-column-form.html')
