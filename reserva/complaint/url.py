from django.conf.urls import url
from complaint import views

urlpatterns = [
    url('post_compaints/', views.post_complaints),
    url('post_replay/(?P<idd>\w+)', views.post_replay),
    url('view_complaint/', views.view_complaint),
    url('view_replay/', views.view_replay),
    url('userv_compl/', views.user_view_complaint),
    url('uv_reply/', views.user_view_reply),
    url('dltcomp/(?P<idd>\w+)', views.delete_complaint),
    # url('rep/(?P<idd>\w+)', views.post_replay)
]
