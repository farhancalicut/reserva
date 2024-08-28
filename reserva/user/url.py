from django.conf.urls import url
from user import views

urlpatterns = [
    url('post_user/', views.post_user),
    url('view_user/', views.view_user),
    url('profile/', views.post_profile),
    url('post_tutorial/', views.post_tutorial),
    url('post_totorial2/', views.post_tutorial2),
    url('post_totorial3/', views.post_tutorial3),
    url('post_totorial4/', views.post_tutorial4)
]

