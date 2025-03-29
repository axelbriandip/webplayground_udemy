from django.views.generic import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        # Custom logic can be added here if needed
        return render(request, self.template_name, {'title': 'Title Home Page', 'subheading': 'Subheading Home Page'})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"