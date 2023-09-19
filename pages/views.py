from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required # alt: login_required
from django.utils.decorators import method_decorator
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

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch') # Esto hace lo mismo que el mixin
class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name='dispatch') # Esto hace lo mismo que el mixin
class PageUpdateView(UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = "_update_form"

    # Si queremos que al editar, vuelva a la lista de páginas..
    # success_url = reverse_lazy('pages:pages')

    # Si queremos que al editar, dé el OK..
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch') # Esto hace lo mismo que el mixin
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')