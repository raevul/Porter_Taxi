from django.shortcuts import render
from django.views.generic import View
import cloudinary.uploader

from .models import Car


class ServicesView(View):
    def get(self, request, *args, **kwargs):
        try:
            services = Car.objects.all()
            for service in services:
                service.image = cloudinary.utils.cloudinary_url(service.image.url)[0]
        except Exception as e:
            return render(request, "main/error.html")
        context = {
            'services': services
        }
        return render(request, "main/index.html", context=context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/about.html')
