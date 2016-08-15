from django.conf.urls import url
from views import HomeView

urlpatterns = [
    url('^$', HomeView.as_view(), name='home'),
    url('^/result/$', HomeView.as_view(), name='home'),

]
