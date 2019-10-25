from django.conf.urls import url
from fplapp import views

app_name = 'fplapp'
urlpatterns = [
  # The home view ('/fpl/')
  url(r'^$', views.home, name='home'),
  # Explicit home ('/fpl/home/')
  url(r'^home.html$', views.home, name='home'),
  url(r'^playerperformance.html$', views.player_performance, name='player_performance'),
  url(r'^teamperformance.html$', views.team_performance, name='team_performance'),
  url(r'^fixturedifficulty.html$', views.fixture_difficulty, name='fixture_difficulty'),
  url(r'^ict.html$', views.ict, name='ict'),
  url(r'^injury_suspension.html$', views.injury_suspension, name='injury_suspension'),
  url(r'^pricechange.html$', views.price_change, name='price_change'),
  url(r'^topmanagers.html$', views.top_managers, name='top_managers'),
  url(r'^transfers.html$', views.transfer_in_out, name='transfer_in_out'),
  url(r'^analysis.html$', views.analysis, name='analysis'),
  url(r'^bot.html$', views.bot, name='bot'),
  url(r'^ranking.html$', views.ranking, name='rank'),
  url(r'^contact.html$', views.email_view, name='email'),
  url(r'^success/$', views.success_view, name='email_success'),
  url(r'^fixtures.html$', views.match_fixtures, name='fixtures'),
  url(r'^fplstats.html$', views.fpl_stats, name='fpl_stats'),
  url(r'^register.html$', views.register, name='register'),
  url(r'^login.html$', views.login_request, name='login_request'),
  url(r'^logout.html$', views.logout_request, name='logout_request'),
  url(r'^winners.html$', views.winners, name='winners'),
  url(r'^test.html$', views.test, name='test'),
]
