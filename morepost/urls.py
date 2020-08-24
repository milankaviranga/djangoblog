from django.conf.urls import url
from morepost import views
from django.urls import path

app_name ='morepost'

urlpatterns = [
    
    url(r'^dayend/',views.dayend,name='dayend'),
    url(r'^java/dayend/',views.dayend,name='dayend'),
    url(r'^test/dayend/',views.dayend,name='dayend'),

]