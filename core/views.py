from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "core/home.html"

    # forma #1: opción larga para definir un diccionario de contexto
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["test"] = "123"
    #     return context

    # forma #2: opción corta para definir un diccionario de contexto
    def get(self, request):
        return render(request, self.template_name, { 'test': 'este es el test' })

class SamplePageView(TemplateView):
    template_name = 'core/sample.html'