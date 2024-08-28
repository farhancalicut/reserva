from django.conf.urls import url
from slot import views

urlpatterns = [
    url('add_slot/', views.add_slot),
    url('view_slot/(?P<idd>\w+)', views.view_slot),
    url('dlt_slot/(?P<idd>\w+)', views.delete_slot),
]
