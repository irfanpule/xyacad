import sweetify
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from addons import get_addons_list


@login_required
def home(request):
    sweetify.toast(
        request, 'Welcome to home page', icon='info', persistent="Bye toast!")
    context = {
        'addons_list': get_addons_list()
    }
    return render(request, 'dashboard/home.html', context)


def form_general(request):
    return render(request, 'dashboard/two-column-form.html')
