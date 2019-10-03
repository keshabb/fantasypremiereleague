from django.conf.urls import url
from fplapp import views

app_name = 'fplapp'
urlpatterns = [
  # The home view ('/fpl/')
  url(r'^$', views.home, name='home'),
  # Explicit home ('/fpl/home/')
  url(r'^home/$', views.home, name='home'),
]