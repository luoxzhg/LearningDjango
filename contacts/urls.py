from django.conf.urls import url
from . import views

app_name = 'contacts'

urlpatterns = [
    url(r'^$', views.ListContactView.as_view(),
        name='contacts-list'),
    url(r'^new/$', views.CreateContactView.as_view(),
        name='contacts-new'),
    url(r'^edit/(?P<pk>\d+)/$', views.UpdateContactView.as_view(),
        name='contacts-edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteContactView.as_view(),
        name='contacts-delete'),
    url(r'^(?P<pk>\d+)/$', views.DetailContactView.as_view(),
        name='contacts-view'),
    url(r'^edit/(?P<pk>\d+)/addresses$', views.EditContactAddressView.as_view(),
        name='contacts-edit-addresses'),
    
]
