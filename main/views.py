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
            service_url = request.build_absolute_uri(service.get_absolute_url())
        except Exception as e:
            return render(request, "main/error.html")
        context = {
            'services': services,
            'service_url': service_url,
        }
        return render(request, "main/index.html", context=context)


class ServiceDetailView(View):
    def get(self, request, *args, **kwargs):
        try:
            service = Car.objects.get(slug=kwargs['slug'])
        except Exception as e:
            return render(request, 'main/error.html')
        context = {
            'service': service
        }
        return render(request, 'main/service_detail.html', context=context)
