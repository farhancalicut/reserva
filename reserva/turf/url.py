from django.conf.urls import url
from turf import views

urlpatterns = [
    url('post_turf/', views.post_turf),
    url('view_turf/', views.view_turf),
    url('view manageturf',views.view_manageturf),
    url('aprov/(?P<idd>\w+)', views.approve),
    url('reject/(?P<idd>\w+)', views.reject),
    url('manv_turf/', views.manager_viewturf),
    url('map/(?P<idd>\w+)',views.map)
]
