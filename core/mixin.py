from django.views.generic.base import ContextMixin


class ContextMixin(ContextMixin):
    title_page = ''
    sub_title = ''
    btn_submit_name = ''

    def get_title_page(self):
        return self.title_page

    def get_sub_title_page(self):
        return self.sub_title

    def get_btn_submit_name(self):
        return self.btn_submit_name

    def get_context_data(self, **kwargs):
        kwargs['title'] = self.get_title_page()
        kwargs['title_page'] = self.get_title_page()
        kwargs['sub_title_page'] = self.get_sub_title_page()
        kwargs['btn_submit_name'] = self.get_btn_submit_name()
        return super().get_context_data(**kwargs)


class FormFilterMixin(ContextMixin):
    form_filter = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form_filter = self.form_filter(self.request.GET or None)
        context["form_filter"] = form_filter

        if self.request.GET and form_filter.is_valid():
            context.update(form_filter.cleaned_data)

        return context
