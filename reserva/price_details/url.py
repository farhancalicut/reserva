from django.conf.urls import url
from price_details import views

urlpatterns = [
    url('post_price/', views.post_price),
    url('view_pricedetails/', views.view_pricedetails),
    url('view_rite/', views.view_rate),
]
