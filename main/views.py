from django.shortcuts import render
from django.views.generic import View

from .models import Car


class ServicesView(View):
    def get(self, request, *args, **kwargs):
        try:
            services = Car.objects.all()
        except Exception as e:
            return render(request, "main/error.html")
        context = {
            'services': services
        }
        return render(request, "main/index.html", context=context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/about.html')
