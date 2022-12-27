from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views import View
# Create your views here.

monthly_challenges = {
    "january": "January month",
    "february": "February month",
    "march": "March month",
    "april": "April month",
    "may": "May month",
    "june": "June month",
    "july": "July month",
    "august": "August month",
    "september": "september month",
    "october": "October month",
    "november": "Novomber month",
    "december": "December month"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys)
    redirect_month = months[month]
    return HttpResponseRedirect('/main/' + redirect_month)


def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound('This month is not supported')