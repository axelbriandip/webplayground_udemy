from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Page
from .forms import PageForm

# Create your views here.
class PageListViews(ListView):
    model = Page

class PageDetailViews(DetailView):
    model = Page

class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order']
    # def get_success_url(self):
    #     return reverse('pages:pages')
    success_url = reverse_lazy('pages:pages')

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")