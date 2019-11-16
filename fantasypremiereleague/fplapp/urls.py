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
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^teamstats.html$', views.PlotView.as_view(), name='plot'),
  url(r'^plot/$', views.PlotView.as_view(), name='plot'),
  url(r'^plot1d/$', views.Plot1DView.as_view(), name='plot1d'),
  url(r'^plot2d/$', views.Plot2DView.as_view(), name='plot2d'),
  url(r'^plot3d/$', views.Plot3DView.as_view(), name='plot3d'),
  url(r'^plot1d_multiple/(?P<n>\d+)/$',
      views.Plot1DMultipleView.as_view(), name='plot1d_multiple'),
  url(r'^plot1d_multiple_ajax/(?P<n>\d+)/$',
      views.plot1d_multiple_ajax, name='plot1d_multiple_ajax'),
  url(r'^plotIq/$', views.PlotIqView.as_view(), name='plotIq'),
  url(r'^plot_live/$', views.PlotLiveView.as_view(), name='plot_live'),
  url(r'^plot_live_update/$', views.plot_live_update, name='plot_live_update'),
  url(r'^plot3d_scatter/$', views.Plot3DScatterView.as_view(), name='plot3d_scatter'),
]
