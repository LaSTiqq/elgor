from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.urls import path
from .views import send
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def sitemap(request):
    sitemap_file_path = os.path.join(BASE_DIR, 'sitemap.xml')
    with open(sitemap_file_path, 'r') as f:
        sitemap_content = f.read()
    return HttpResponse(sitemap_content, content_type='application/xml')


urlpatterns = [
    path('', send),
    path('sitemap.xml', sitemap),
    path('robots.txt', TemplateView.as_view(
        template_name='robots.txt', content_type="text/plain")),
]
