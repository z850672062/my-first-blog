from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list')
    
]