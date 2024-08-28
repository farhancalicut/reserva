from django.conf.urls import url
from manager import views

urlpatterns = [
    url('post_manager/', views.post_manager),
    url('view_managemanager/', views.view_managemanager),
    url('aprv/(?P<idd>\w+)', views.approve),
    url('rej/(?P<idd>\w+)', views.reject),
    url('updtt/', views.updt)
]
