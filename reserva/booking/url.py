from django.conf.urls import url
from booking import views

urlpatterns=[
    url('post_booking/(?P<idd>\w+)', views.post_booking),
    # url('view_cancelturf/', views.view_cancelturf),
    url('view_manage/', views.view_managebooking),
    url('view_booking/', views.view_booking),
    # url('view_bookingstatus/', views.view_bookingstatus),
    url('aprv/(?P<idd>\w+)', views.approve),
    url('rej/(?P<idd>\w+)', views.reject),
    url('can/(?P<idd>\w+)', views.cancel),
    url('uservbook/', views.user_viewbooking)
]
