from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Thread
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ThreadList(TemplateView):
    template_name = 'messenger/thread_list.html'

@method_decorator(login_required, name='dispatch')
class ThreadDetail(DetailView):
    model = Thread

    # verificar si el request.user es parte de los usuarios del hilo
    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404() # en caso de que no sea parte del hilo
        return obj # en caso de que si sea parte del hilo, se retorna el objeto