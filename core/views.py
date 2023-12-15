from django.views.generic.detail import DetailView
from django.views.generic.edit import DeletionMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.forms.models import model_to_dict
from core.mixin import ContextMixin, FormFilterMixin
from core.utils import Logger
from view_breadcrumbs import ListBreadcrumbMixin, CreateBreadcrumbMixin, UpdateBreadcrumbMixin, DetailBreadcrumbMixin


class BaseTemplateView(ContextMixin, TemplateView):
    pass


class BaseFormFilterView(FormFilterMixin, BaseTemplateView):
    pass


class BaseListView(ContextMixin, ListView):
    pass


class BaseCreateView(ContextMixin, CreateView):

    def form_valid(self, form):
        self.object = form.save()
        log = Logger()
        log.addition(self.request, self.object)
        return super().form_valid(form)


class BaseUpdateView(ContextMixin, UpdateView):
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        self.object = form.save()
        log = Logger()
        log.change(self.request, self.object)
        return super().form_valid(form)


class BaseDeleteView(DeletionMixin, DetailView):
    pk_url_kwarg = 'id'

    def delete(self, request, *args, **kwargs):
        log = Logger()
        obj = self.get_object()
        deletion = super().delete(request, *args, **kwargs)
        log.deletion(request, obj)
        return deletion

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class BaseDetailView(ContextMixin, DetailView):
    pk_url_kwarg = 'id'
    template_name = 'general_detail.html'
    specific_sidebar_menu = None

    def get_title_page(self):
        obj = self.get_object()
        return f"Detail data {obj.nama}"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context["object_dict"] = model_to_dict(obj)
        context["specific_sidebar_menu"] = self.specific_sidebar_menu
        return context


class ListBreadcrumbView(LoginRequiredMixin, ListBreadcrumbMixin, BaseListView):
    pass


class CreateBreadcrumbView(LoginRequiredMixin, CreateBreadcrumbMixin, BaseCreateView):

    def form_valid(self, form):
        self.object = form.save()
        log = Logger()
        log.addition(self.request, self.object)
        return super().form_valid(form)


class UpdateBreadcrumbView(LoginRequiredMixin, UpdateBreadcrumbMixin, BaseUpdateView):
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        self.object = form.save()
        log = Logger()
        log.change(self.request, self.object)
        return super().form_valid(form)


class DetailBreadcrumbView(LoginRequiredMixin, DetailBreadcrumbMixin, BaseDetailView):
    pk_url_kwarg = 'id'
    template_name = 'general_detail.html'

    def get_title_page(self):
        obj = self.get_object()
        return f"Detail data {obj}"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context["object_dict"] = model_to_dict(obj)
        return context
