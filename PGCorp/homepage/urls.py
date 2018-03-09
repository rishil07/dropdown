from django.conf.urls import url
from . import views
from .views import FlatView

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^buy/$', FlatView.as_view(), name='flat')
]