from django.urls import path
from . import views as vw

urlpatterns = [
    path('', vw.VW_posts, name='URL_posts'),
    path('post/<int:pk>/', vw.VW_post_detail, name='URL_post_detail'),
]