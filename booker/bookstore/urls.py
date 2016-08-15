from django.conf.urls import url
from views import HomeView,ResultView

urlpatterns = [
    url('^$', HomeView.as_view(), name='home'),
    url('^/result/$', ResultView.as_view(), name='result'),

]
