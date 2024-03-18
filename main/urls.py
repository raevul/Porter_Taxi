from django.urls import path

from .views import ServicesView, ServiceDetailView


urlpatterns = [
    path('', ServicesView.as_view(), name='services'),
    path('<slug:slug>/', ServiceDetailView.as_view(), name='service_detail'),
]
