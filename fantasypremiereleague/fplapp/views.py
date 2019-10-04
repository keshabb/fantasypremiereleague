from django.shortcuts import render
from django.views.decorators.cache import cache_page
from fplapp.ranking import Rank


def home(request):
    return render(request, 'fplapp/home.html')


@cache_page(60 * 10)
def ranking(request):
    rank = Rank()
    rank_table_info = rank.get_team_rank()
    context = {'rank_info': rank_table_info}
    return render(request, 'fplapp/ranking.html', context)


@cache_page(60 * 10)
def player_performance(request):
    return render(request, 'fplapp/player_performance.html')


@cache_page(60 * 10)
def fixture_difficulty(request):
    return render(request, 'fplapp/fixture_difficulty.html')


@cache_page(60 * 10)
def ict(request):
    return render(request, 'fplapp/ict.html')


@cache_page(60 * 10)
def injury_suspension(request):
    return render(request, 'fplapp/injury_suspension.html')


@cache_page(60 * 10)
def price_change(request):
    return render(request, 'fplapp/price_change.html')


@cache_page(60 * 10)
def transfer_in_out(request):
    return render(request, 'fplapp/transfer_in_out.html')


@cache_page(60 * 10)
def top_managers(request):
    return render(request, 'fplapp/top_managers.html')


def analysis(request):
    return render(request, 'fplapp/analysis.html')


def bot(request):
    return render(request, 'fplapp/bot.html')
