from django.conf.urls import url
from assignmanager import views

urlpatterns=[
    url('post_assignmanager/', views.post_assignmanager),
    url('view_assign/', views.view_assign),
    url('post_assign/', views.post_assignmanager),
]
