from django.urls import path
from . import views as vw

urlpatterns = [
    path('', vw.VW_home, name='URL_home'),
    path('contact/', vw.VW_contact, name='URL_contact'),
]