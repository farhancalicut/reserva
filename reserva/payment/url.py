from django.conf.urls import url
from payment import views

urlpatterns = [
     url('post_payment/(?P<idd>\w+)', views.post_payment),
     url('view_payment/', views.view_payment),
     url('userv_pay/', views.user_view_payment),
     url('user_pay_history/', views.user_paymenthistory),
]

