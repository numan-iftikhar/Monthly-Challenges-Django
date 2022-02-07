
from cgitb import html
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
# we write either functions or classes here in views
months_decription = {
    'january': 'Eat no meat for this entire month',
    'february': 'Walk for atleast 20 minutes daily this month',
    'march': 'Learn django for 30 minutes daily',
    'april': 'Eat no meat for this entire month',
    'may': 'Walk for atleast 20 minutes daily this month',
    'june': 'Learn django for 30 minutes daily',
    'july': 'Eat no meat for this entire month',
    'august': 'Walk for atleast 20 minutes daily this month',
    'september': 'Learn django for 30 minutes daily',
    'october': 'Eat no meat for this entire month',
    'november': 'Walk for atleast 20 minutes daily this month',
    'december': 'Learn django for 30 minutes daily',
}

# months_number_decription = {
#     1: 'Eat no meat this month',
#     2: 'Walk Eat no meat this month',
#     3: 'Learn Eat no meat this month',
# }


def index(request):
    """will generate dynamic HTML for all the months with their respective links attached to them"""
    months_str = ""
    # getting all the months' names in a list
    months = list(months_decription.keys())
    # iterating through months list
    for month in months:
        cap_month = month.capitalize()
        # the reverse() function helps us to build urls dynamically without hard-coding them
        # i.e., challenges/january
        month_path = reverse("month-name", args=[month])
        months_str += f"<li><a href='{month_path}'><h2>{cap_month}</h2></a></li>"

    # now we wrap all months in an ordered list
    response_months_str = f"<ol>{months_str}</ol>"
    return HttpResponse(response_months_str)


# this function is only called if the entered month is an int
def month_by_number(request, month):
    '''takes month_number and redirect to that specific month i.e., january for 1'''
    # It will return a list of months
    months = list(months_decription.keys())
    # validating the month
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    # bcz list indexing starts from 0
    redirect_month = months[month - 1]
    # Generating redirect path ie, challenges/january etc
    redirect_path = reverse('month-name', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    '''will return value of entered month'''
    try:
        return HttpResponse(months_decription[month])
    except:
        return HttpResponseNotFound("This month is not supported!")
