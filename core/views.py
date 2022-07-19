from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import DeletionMixin
from core.utils import Logger


class DeleteView(DeletionMixin, BaseDetailView):

    def delete(self, request, *args, **kwargs):
        log = Logger()
        obj = self.get_object()
        deletion = super().delete(request, *args, **kwargs)
        log.deletion(request, obj)
        return deletion

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
