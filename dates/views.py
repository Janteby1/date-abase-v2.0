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
        user_creation_form = UserForm()
        add_date_form = AddDateForm()
        search_date_form_category = SearchDateForm()
        search_date_form_area = SearchDateForm_Area()
        search_date_form_price = SearchDateForm_Price()

        context = {
            'user_creation_form': user_creation_form,
            "add_date_form":add_date_form,
            "search_date_form_category":search_date_form_category,
            "search_date_form_area":search_date_form_area,
            "search_date_form_price": search_date_form_price,
            }

        return render(request, "index.html", context)


# class About(View):
#     def get(self, request):
#         return render(request, "about.html")


        