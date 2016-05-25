from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseForbidden
from django.http import JsonResponse
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .forms import AddDateForm, SearchDateForm_Category, UserForm, LoginForm, SearchDateForm_Area, SearchDateForm_Price
from .models import UserProfile, Dates 


# Create your views here.
class Landing(View):
    def get(self, request):
        return render(request, "landing.html")

class Index(View):
    def get(self, request):
        user_creation_form = UserForm()
        login_form = LoginForm()
        # add_date_form = AddDateForm()
        search_date_form_category = SearchDateForm_Category()
        search_date_form_area = SearchDateForm_Area()
        search_date_form_price = SearchDateForm_Price()

        context = {
            'user_creation_form': user_creation_form,
            'login_form': login_form,
            # "add_date_form":add_date_form,
            "search_date_form_category":search_date_form_category,
            "search_date_form_area":search_date_form_area,
            "search_date_form_price": search_date_form_price,
            }

        return render(request, "index.html", context)


class User_Register(View):
    def post(self, request):
        if request.is_ajax():
            data = request.POST
        else:
            body = request.body.decode()
            if not body: 
                return JsonResponse ({"response":"Missing Body"})
            data = json.loads(body)

        user_form = UserForm(data)
        if user_form.is_valid():
            user = user_form.save()
            return JsonResponse({"Message": "Register succesfull", "success": True})
        else:
            return JsonResponse ({"response":"Invalid information", 'success' : False, 'errors': user_form.errors })


class User_Login(View):
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session.set_expiry(30000)
            return JsonResponse({"username":user.username, "success": True})
        else:
            return JsonResponse({'errors': form.errors})


class User_Logout(View):
    def post(self, request):
        print(request)
        logout(request) # django built in logout 
        return JsonResponse ({"Message":"Logout Successful"})


class AddDate(View):
    def post(self, request):
        # checks to make sure the user is logged in 
        if request.user.is_authenticated():
            form = AddDateForm(request.POST)
            form.is_valid()
            # add the user to each post 
            user = request.user
            date = form.save(commit=False)
            date.user = user
            date.save()
            return JsonResponse({"Message":"added date", "success": True})
        else:
            return JsonResponse({"success": False})

        if request.is_ajax():
            data = request.POST
        else:
            body = request.body.decode()
            if not body: 
                return JsonResponse ({"response":"Missing Body"})
            data = json.loads(body)

        user_form = UserForm(data)
        if user_form.is_valid():
            user = user_form.save()
            return JsonResponse({"Message": "Register succesfull", "success": True})


class SearchDate_Price(View):
    # need to pass the check box values to the db and retun the date ideas
    def post(self, request):
        if request.is_ajax():
            data = request.POST
        else:
            body = request.body.decode()
            if not body: 
                return JsonResponse ({"response":"Missing Body"})
            data = json.loads(body)
        
        form = SearchDateForm_Price(request.POST)
        if form.is_valid():
            # this gets all the values the user checked
            codes=data.get("price")

            # this returns a list of all the date ideas returned from the db 
            dates = Dates.objects.filter(price=codes)
            # put all the values into a json dictionary with a method called from the models
            dates = [date.to_json() for date in dates]

            if dates:
                return JsonResponse({
                    "success": True, 'results': dates})
            else:
                return JsonResponse({"success": True})
        else:
            return JsonResponse ({"Message":"Invalid information", 'success' : False })


class SearchDate_Category(View):
    def post(self, request):
        if request.is_ajax():
            data = request.POST
        else:
            body = request.body.decode()
            if not body: 
                return JsonResponse ({"response":"Missing Body"})
            data = json.loads(body)
        
        form = SearchDateForm_Category(request.POST)
        if form.is_valid():
            # this gets all the values the user checked
            codes=data.get("category")

            # this returns a list of all the date ideas returned from the db 
            dates = Dates.objects.filter(category=codes)
            # put all the values into a json dictionary with a method called from the models
            dates = [date.to_json() for date in dates]

            if dates:
                return JsonResponse({
                    "success": True, 'results': dates})
            else:
                return JsonResponse({"success": True})
        else:
            return JsonResponse ({"Message":"Invalid information", 'success' : False })


class SearchDate_Area(View):
    def post(self, request):
        if request.is_ajax():
            data = request.POST
        else:
            body = request.body.decode()
            if not body: 
                return JsonResponse ({"response":"Missing Body"})
            data = json.loads(body)
        
        form = SearchDateForm_Area(request.POST)
        if form.is_valid():
            # this gets all the values the user checked
            codes=data.get("area")

            # this returns a list of all the date ideas returned from the db 
            dates = Dates.objects.filter(area=codes)
            # put all the values into a json dictionary with a method called from the models
            dates = [date.to_json() for date in dates]

            if dates:
                return JsonResponse({"success": True, 'results': dates})
            else:
                return JsonResponse({"success": True})
        else:
            return JsonResponse ({"Message":"Invalid information", 'success' : False })


class Delete_Date(View):
    def post(self, request, dates_id=None):
        date = Dates.objects.get(id=dates_id)

        if request.user.is_authenticated():
            date.show = False
            date.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False})


class Vote_Up_Date(View):
    def post(self, request, dates_id=None):
        date = Dates.objects.get(id=dates_id)

        if request.user.is_authenticated():
            date.vote += 1
            date.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False})

class Vote_Down_Date(View):
    def post(self, request, dates_id=None):
        date = Dates.objects.get(id=dates_id)

        if request.user.is_authenticated():
            date.vote -= 1
            date.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False})

class Top_Dates(View):
    def get(self, request, dates_slug=None):
        # this line gets all the posts that we have in the db and orders them by top votes
        dates = Dates.objects.filter(show=True).order_by('-vote')[:15]
        # put all the values into a json dictionary with a method called from the models
        dates = [date.to_json() for date in dates]

        return JsonResponse({"success": True, 'results': dates})



        