from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^remove/(?P<course_id>\d+)$', views.confirm_remove),
]