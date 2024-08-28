from django.conf.urls import url
from feedback import views

urlpatterns = [
    url('post_feedback/', views.post_feedback),
    url('feed_view/', views.view_feed),
    url('manager_vw_feed/',views.veiw_feeds_manager),
    url('view_feed_admin/',views.view_feed_afmin),
]
