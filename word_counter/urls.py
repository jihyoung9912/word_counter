from unicodedata import name
import django


from django.urls import URLPattern, path
from.import views


urlpatterns = [
    path("", views.index,name='index'),
    path("result",views.result,name='result')
]   
