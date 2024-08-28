from django.conf.urls import url
from temp import views

urlpatterns=[
    url('admin/', views.admin),
    url('home/', views.home),
    url('manager/', views.manager),
    url('user/', views.user),
    url('usr_2hme/',views.user_2_home),
    url('mangr_2hom/',views.manager_2_home),
    url('amin_2_hoe/',views.admin_2_home),
    url('home_base/', views.home_base),
    url('view_feed/', views.view_turf)
]
