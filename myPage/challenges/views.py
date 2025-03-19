from django.shortcuts import render
from django.http import HttpResponseNotFound,Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

challenges = {
    "january": "Eat no meat for the entire month.",
    "february": "Walk for at least 20 minutes every day.",
    "march": "Learn Django for at least 20 minutes every day.",
    "april": "Eat no meat for the entire month.",
    "may": "Walk for at least 20 minutes every day.",
    "june": "Learn Django for at least 20 minutes every day.",
    "july": "Eat no meat for the entire month.",
    "august": "Walk for at least 20 minutes every day.",
    "september": "Learn Django for at least 20 minutes every day.",
    "october": "Eat no meat for the entire month.",
    "november": "Walk for at least 20 minutes every day.",
    "december": None
}

# Challenges index page listing all the challenge months
def challenges_index(request):
    months = list(challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


# Challenge page for a specific month by number
def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    #return monthly_challenge(request, months[month-1])
    else:
        redirect_path = reverse("month-challenge", args=[months[month-1]])
        return HttpResponseRedirect(redirect_path)
    

# Challenge page for a specific month
def monthly_challenge(request, month):
    try:
        challenge_month = challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "challenge": challenge_month,
        })
    except:
        raise Http404()