from django.conf.urls import url
from views import HomeView

urlpatterns = [
    url('^$', HomeView.as_view(), name='home'),
]
