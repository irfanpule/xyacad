from django.views.generic.detail import BaseDetailView, DetailView
from django.views.generic.edit import DeletionMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from core.mixin import ContextMixin
from core.utils import Logger


class ListView(ContextMixin, ListView):
    pass


class CreateView(ContextMixin, CreateView):

    def form_valid(self, form):
        self.object = form.save()
        log = Logger()
        log.addition(self.request, self.object)
        return super().form_valid(form)


class UpdateView(ContextMixin, UpdateView):
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


class DetailView(ContextMixin, DetailView):
    pk_url_kwarg = 'id'

    def get_title_page(self):
        obj = self.get_object()
        return f"Detail data {obj.nama}"
