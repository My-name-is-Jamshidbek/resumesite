from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
