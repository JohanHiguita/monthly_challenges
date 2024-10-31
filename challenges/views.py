from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Jan Challenge",
    "february": "Feb challenge",
    "march": "march challenge",
    "april": "Apr challenge",
    "june": "Jun challenge",
    "july": "Jul challenge",
    "august": "Aug challenge",
    "september": "sep challenge",
    "october": "oct challenge",
    "november": "nov challenge",
    "december": "dec challenge"
}


def monthly_challenge(request, month):
    challenge_text = None
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound(f"month {month} is not supported")


def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # challenge/january
    # return HttpResponseRedirect(f"/challenges/{redirect_month}")
    return HttpResponseRedirect(redirect_path)
