from django.conf.urls import url
from responder import views

urlpatterns = [

    url(r'^contents/$',views.ContentList.as_view())

]