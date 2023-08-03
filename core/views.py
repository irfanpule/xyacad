from django.views.generic.detail import BaseDetailView, DetailView
from django.views.generic.edit import DeletionMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.forms.models import model_to_dict
from core.mixin import ContextMixin
from core.utils import Logger
from view_breadcrumbs import ListBreadcrumbMixin, CreateBreadcrumbMixin, UpdateBreadcrumbMixin, DetailBreadcrumbMixin


class ListView(ListBreadcrumbMixin, ContextMixin, ListView):
    pass


class CreateView(CreateBreadcrumbMixin, ContextMixin, CreateView):

    def form_valid(self, form):
        self.object = form.save()
        log = Logger()
        log.addition(self.request, self.object)
        return super().form_valid(form)


class UpdateView(UpdateBreadcrumbMixin, ContextMixin, UpdateView):
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        self.object = form.save()
        log = Logger()
        log.change(self.request, self.object)
        return super().form_valid(form)


class DeleteView(DeletionMixin, BaseDetailView):
    pk_url_kwarg = 'id'

    def delete(self, request, *args, **kwargs):
        log = Logger()
        obj = self.get_object()
        deletion = super().delete(request, *args, **kwargs)
        log.deletion(request, obj)
        return deletion

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class DetailView(DetailBreadcrumbMixin, ContextMixin, DetailView):
    pk_url_kwarg = 'id'
    template_name = 'general_detail.html'

    def get_title_page(self):
        obj = self.get_object()
        return f"Detail data {obj.nama}"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context["object_dict"] = model_to_dict(obj)
        return context
