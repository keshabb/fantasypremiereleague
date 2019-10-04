from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from fplapp.ranking import Rank
from fplapp.forms import ContactForm


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


def email_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['test@example.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return redirect("success")
    return render(request, "fplapp/contact.html", {'form': form})


def success_view(request):
    return HttpResponse('Success! Thank you for your message.')
