from django.views.generic.base import ContextMixin


class ContextMixin(ContextMixin):
    title_page = ''
    sub_title = ''
    btn_submit_name = ''
    active_menu = ''

    def get_title_page(self):
        return self.title_page

    def get_sub_title_page(self):
        return self.sub_title

    def get_btn_submit_name(self):
        return self.btn_submit_name

    def get_active_menu(self):
        return self.active_menu

    def get_context_data(self, **kwargs):
        kwargs['title'] = self.get_title_page()
        kwargs['title_page'] = self.get_title_page()
        kwargs['sub_title_page'] = self.get_sub_title_page()
        kwargs['btn_submit_name'] = self.get_btn_submit_name()
        kwargs['active_menu'] = self.get_active_menu()
        return super().get_context_data(**kwargs)


class FormFilterMixin(ContextMixin):
    form_filter = None
    form_filter_fields = {}

    def dispatch(self, request, *args, **kwargs):
        form_filter = self.form_filter(self.request.GET or None)
        if request.GET and form_filter.is_valid():
            self.form_filter_fields = form_filter.cleaned_data
            print("filter fields", self.form_filter_fields)
        else:
            print("filter field", self.form_filter_fields)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.form_filter()
        context.update(self.get_form_filter_fields())
        return context

    def get_form_filter_fields(self):
        return self.form_filter_fields
