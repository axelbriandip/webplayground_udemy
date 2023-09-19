from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Page

# Create mixin
class StaffRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class PagesListView(ListView):
    model = Page

class PageDetailView(StaffRequiredMixin, DetailView):
    model = Page

class PageCreateView(StaffRequiredMixin, CreateView):
    model = Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')

class PageUpdateView(StaffRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = "_update_form"

    # Si queremos que al editar, vuelva a la lista de páginas..
    # success_url = reverse_lazy('pages:pages')

    # Si queremos que al editar, dé el OK..
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

class PageDeleteView(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')