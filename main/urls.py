from django.urls import path

from .views import ServicesView, AboutView


urlpatterns = [
    path('', ServicesView.as_view(), name='services'),
    path('about/', AboutView.as_view(), name='about'),
]
