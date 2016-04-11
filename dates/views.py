from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseForbidden
from django.http import JsonResponse
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import AddDateForm, SearchDateForm, UserForm, SearchDateForm_Area, SearchDateForm_Price
from .models import UserProfile, Dates 


# Create your views here.
class Index(View):
    def get(self, request):
        # create blank conext incase someone isnt signed in already 
        context = {}
        # check to see if someone is already logged in
        if request.user.is_authenticated(): 
            # get their username  
            username = request.user.username
            message = ("Hello, " + username)
            # send them a greating so they know they are signed in 
            context = {
                'message': message,}

        # this line gets all the posts that we have in the db and orders them by most recent
        dates = Dates.objects.filter(show=True).order_by('-count')[:15]
        # put all the dates into a context dict
        context ["dates"] = dates

        # send them all to the template
        return render(request, "index.html", context)


class About(View):
    def get(self, request):
        return render(request, "about.html")


        