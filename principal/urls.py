from django.urls import path
from principal.views import index_view


urlpatterns = [
	path('', index_view, name='index'),
]
