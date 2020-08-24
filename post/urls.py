from django.conf.urls import url
from post import views
from django.urls import path

app_name ='post'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^java/',views.java,name='java'),
    url(r'^python/',views.pythons,name='pythons'),
    url(r'^test/',views.tests,name='tests'),
    url(r'^follow/',views.formes,name='formes')

]