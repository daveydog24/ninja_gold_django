from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money$', views.process_money),
    url(r'^reset$', views.reset)
]