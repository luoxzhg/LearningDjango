from django.conf.urls import url
from . import views

app_name = 'weblog'

urlpatterns=[
    url('^categories/(?P<slug>[\w-]+/$', views.CategoryDetail.as_view(), name='category-detail'),
    
]
