from django.urls import path
from django.views.generic import TemplateView
from .views import games


urlpatterns = [
    path('platform/', TemplateView.as_view(template_name='fourth_task/platform.html')),
    path('platform/games/', games),
    path('platform/cart/', TemplateView.as_view(template_name='fourth_task/cart.html')),
]
