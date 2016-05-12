from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, CheckboxInput, PasswordInput
from dates.models import Dates

from .models import UserProfile, Dates

AREAS = (  
    ('Allenhurst', "Allenhurst"),
    ('Asbury', "Asbury"),
    ('Astoria', "Astoria"),
    ('Atlantic City', "Atlantic City"),
    ('Bay Ridge', "Bay Ridge"),
    ('Borough Park', "Borough Park"),
    ('Bradley', "Bradley"),
    ('Bronx', "Bronx"),
    ('Brooklyn', "Brooklyn"),
    ('Brooklyn Hieghts', "Brooklyn Hieghts"),
    ('Caroll Gardens', "Caroll Gardens"),
    ('Central Park', "Central Park"),
    ('Chelsea', "Chelsea"),
    ('Cobble Hill', "Cobble Hill"),
    ('Coney Island', "Coney Island"),
    ('Crown Hieghts', "Crown Hieghts"),
    ('Deal', "Deal"),
    ('Dumbo', "Dumbo"),
    ('East Rutherford', "East Rutherford"),
    ('Eatontown', "Eatontown"),
    ('Edison', "Edison"),
    ('Elizabeth', "Elizabeth"),
    ('Financial District', "Financial District"),
    ('Five Towns', "Five Towns"),
    ('Flatiron', "Flatiron"),
    ('Greenich Village', "Greenich Village"),
    ('Greatneck', "Greatneck"),
    ('Hazlet', "Hazlet"),
    ('Jackson', "Jackson"),
    ('Various', "Various"),
    ('IDEA', "Idea"),
    ('Park', "Park"),
    ('Keansburg', "Keansburg"),
    ('Kips Bay', "Kips Bay"),
    ('Lakewood', "Lakewood"),
    ('Lenox Hill', "Lenox Hill"),
    ('Long Island', "Long Island"),
    ('Malboro', "Malboro"),
    ('Midtown', "Midtown"),
    ('Monsey', "Monsey"),
    ('Mt Vernon', "Mt Vernon"),
    ('New Rochelle', "New Rochelle"),
    ('Newark', "Newark"),
    ('Oakhurst', "Oakhurst"),
    ('Park Slope', "Park Slope"),
    ('Point Pleasant', "Point Pleasant"),
    ('Prospect Park', "Prospect Park"),
    ('Queens', "Queens"),
    ('Red Bank', "Red Bank"),
    ('Seaside Hieghts', "Seaside Hieghts"),
    ('Staten Island', "Staten Island"),
    ('Tinton Falls', "Tinton Falls"),
    ('Union Square', "Union Square"),
    ('Upper East Side', "Upper East Side"),
    ('West Village', "West Village"),
    ('Williamsburg', "Williamsburg"),
    )

PRICES = (  
    ('$', "$"),
    ('$$', "$$"),
    ('$$$', "$$$"),
    ('$$$$', "$$$$"),
    ) 


# Layout
# CHOICES = [('Form name','Database name'),]
# in the form there are two choice that correspond to the same db input (35-64)
STATE_CHOICES = [('ny',"state"), ('nj',"state"), ('other',"state")]
PARKING_CHOICES = [('on',"parking"), ('off',"parking")]
# CATEGORY_CHOICES = CATEGORIES = (('ACT1', "ACT1"), ('ACT2', "ACT2"), ('ACT3', "ACT3"), ('ACT4', "ACT4"), ('ACT5', "ACT5"), ('ACT6', "ACT6"),('ACT7', "ACT7"), ('ACT8', "ACT8"), ('ACT9', "ACT9"), ('ACT10', "ACT10"), ('ACT11', "ACT11"), ('ACT12', "ACT12"), ('ACT13', "ACT13"), ('ACT14', "ACT14"), ('ACT15', "ACT15"), ('ACT16', "ACT16"),('ACT17', "ACT17"), ('ACT18', "ACT18"), ('ACT19', "ACT19"), ('ACT20', "ACT20"), ('ACT21', "ACT21"), ('ACT22', "ACT22"), ('AMU', 'AMU'),('DES', 'DES'),('DES_P', 'DES_P'),('DIN_D', 'DIN_D'),('DIN_Deal', 'DIN_Deal'),('DIN_M', 'DIN_M'),('LUN', 'LUN'),('STA', 'STA'),('WEB', 'WEB'))
CATEGORY_CHOICES = CATEGORIES = (('ACT1', "category"), ('ACT2', "category"), ('ACT3', "category"), ('ACT4', "category"), ('ACT5', "category"), ('ACT6', "category"),('ACT7', "category"), ('ACT8', "category"), ('ACT9', "category"), ('ACT10', "category"), ('ACT11', "category"), ('ACT12', "category"), ('ACT13', "category"), ('ACT14', "category"), ('ACT15', "category"), ('ACT16', "category"),('ACT17', "category"), ('ACT18', "category"), ('ACT19', "category"), ('ACT20', "category"), ('ACT21', "category"), ('ACT22', "category"), ('AMU', 'category'),('DES', 'category'),('DES_P', 'category'),('DIN_D', 'category'),('DIN_Deal', 'category'),('DIN_M', 'category'),('LUN', 'category'),('STA', 'category'),('WEB', 'category'))

class AddDateForm(forms.Form):
    place = forms.CharField() # get the input directly from the user
    address = forms.CharField() # get the input directly from the user
    area = forms.CharField() # get the input directly from the user
    state = forms.ChoiceField(
        choices = STATE_CHOICES,
    )
    category = forms.ChoiceField(
        choices = CATEGORY_CHOICES,
    )
    price = forms.CharField() # get the input directly from the user
    parking = forms.ChoiceField(
        choices = PARKING_CHOICES,
    )
    phone = forms.CharField() # get the input directly from the user
    website = forms.CharField() # get the input directly from the user
    notes = forms.CharField() # get the input directly from the user

    def save(self, commit=True):
        date = Dates(**self.cleaned_data)
        if commit == True:
            date.save()
        return date

# form used to register a user
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]
        widgets = {
            # this sets the input text area
            "password": PasswordInput(),
        }


# need a search form to get date ideas by catergory using check boxes
class SearchDateForm(forms.ModelForm):   
    category_choice = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=CATEGORIES)

    class Meta:
        model = Dates

        fields = [
            "category_choice", 
        ]


class SearchDateForm_Area(forms.ModelForm):   
    area_choice = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=AREAS)

    class Meta:
        model = Dates

        fields = [
            "area_choice", 
        ]

class SearchDateForm_Price(forms.ModelForm):   
    price_choice = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=PRICES)

    class Meta:
        model = Dates

        fields = [
            "price_choice", 
        ]






