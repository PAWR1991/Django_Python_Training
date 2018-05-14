from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^books$', views.home),
	url(r'^books/add$', views.addpage),
	url(r'^addbook$', views.addbook),
	# url(r'^bookspage$', views.bookspage),
    url(r'^books/(?P<id>\d+)$', views.bookspage),
    
]
# (?P<id>\d+)