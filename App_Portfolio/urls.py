from django.urls import path
from . import views as vw

urlpatterns = [
    path('', vw.VW_home, name='URL_home'),
]