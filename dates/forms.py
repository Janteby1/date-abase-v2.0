from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, CheckboxInput, PasswordInput

from .models import UserProfile, Dates

CATEGORIES = (  
    ('ACT1', 'Acrobatic'),
    ('ACT2', 'Arcade'),
    ('ACT3', 'Archery'),
    ('ACT4', 'Bar'),
    ('ACT5', 'Billiards'),
    ('ACT6', 'Boat Rental'),
    ('ACT7', 'Boat'),
    ('ACT8', 'Bowling'),
    ('ACT9', 'Bucket List'),
    ('ACT10', 'Chill'),
    ('ACT11', 'Experience'),
    ('ACT12', 'Go Karting'),
    ('ACT13', 'Horseback Riding'),
    ('ACT14', 'Ice Skating'),
    ('ACT15', 'Karaoke'),
    ('ACT16', 'Mini Golf'),
    ('ACT17', 'Movies'),
    ('ACT18', 'Musuem'),
    ('ACT19', 'Painting'),
    ('ACT20', 'Park'),
    ('ACT21', 'Play'),
    ('ACT22', 'Zoo'),

    ('AMU', 'Amusement Park'),
    ('DES', 'Dessert (D)'),
    ('DES_P', 'Dessert (D/P)'),
    ('DIN_D', 'Dinner (D)'),
    ('DIN_Deal', 'Dinner (Deal)'),
    ('DIN_M', 'Dinner (M)'),
    ('LUN', 'Lunch (D)'),
    ('STA', 'Stadium'),
    ('WEB', 'Website'),
    )


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












# Layout
# CHOICES = [('Form name','Database name'),]

# in the form there are two choice that correspond to the same db input (35-64)
AGE_CHOICES = [('0_19',"age_0_19"), ('20_24',"age_20_24"), ('25_34',"age_25_34"), ('35_54',"age_35_64"), ('55_64',"age_35_64"), ('65+',"age_65_over")]
GENDER_CHOICES = [('male',"gender_m"), ('female', "gender_f")]
# there is no children field in the db 
NUMBER_OF_CHILDREN_CHOICES = [('none','0'), ('1_plus','1_2'), ('3_plus','3_plus')]
CURRENT_EDU_LEVEL_CHOICES = [('elementary','school_enrollment_pre_highschool'), ('hs','school_enrollment_highschool'), ('college','school_enrollment_college')]
HIGHEST_EDU_LEVEL_CHOICES = [('hs_plus','education_highschool_over'), ('college_plus','education_college_over')]
MARITAL_STATUS_CHOICES = [('on','married'), ('off','divorced')]
NUMBER_OF_UNITS_CHOICES = [('0_2','number_of_units_2_less'), ('3_10','number_of_units_3_10'), ('10_+','number_of_units_10_plus')]
OWNERSHIP_TYPE_CHOICES = [('rent','resident_type_renter'), ('purchase','resident_type_owner')]
NUMBER_OF_ROOMS_CHOICES = [('1_room','rooms_per_unit_1'), ('2_room','rooms_per_unit_2'),('3_5_room','rooms_per_unit_3_5'), ('6_plus','rooms_per_unit_6_plus')]
BUILDING_AGE_CHOICES = [('pre_1970','constucted_before_1970'), ('post_1970','constucted_1970_2000'), ('2000+','constucted_after_2000')]
NUMBER_OF_VEHICLES_CHOICES = [('off','vehicles_0'), ('on','vehicles_1'), ('on','vehicles_2_plus')]
# there is no commute types field in the db 
COMMUTE_TYPE_CHOICES = [('walk','walk'), ('transit','transit'), ('drive','drive')]
# these two feilds go into the school score table
SCHOOL_LEVEL_CHOICES = [
    ('school_k-','k_school_score'), ('school_1-8','elem_school_score'), ('school_hs','hs_school_score'), 
    # ('school_none','none')
]
SCHOOL_QUALITY_CHOICES = [('not_high','not_high'), ('high','high'), ('very_high','very_high')]
NIGHT_LIFE_CHOICES = [('not_high','night_life_score'), ('high','night_life_score'), ('very_high','night_life_score')]
NOISE_LEVEL_CHOICES = [('off','noise_score'), ('on','noise_score')]
CRIME_LEVEL_CHOICES = [('off','crime_score'), ('on','crime_score')]
BOROUGH_CHOICES = [('Brooklyn','Brooklyn'),('Bronx','Bronx'),('Manhattan','Manhattan'),('Queens','Queens'),('Staten_Island','Staten Island'),]

class AddDateForm(forms.ModelForm):
    age = forms.ChoiceField(
        choices = AGE_CHOICES,
    )
    gender = forms.ChoiceField(
        choices = GENDER_CHOICES,
    )
    number_of_children = forms.ChoiceField(
        choices = NUMBER_OF_CHILDREN_CHOICES,
    )
    current_edu_level = forms.ChoiceField(
        choices = CURRENT_EDU_LEVEL_CHOICES,
    )
    highest_edu_level = forms.ChoiceField(
        choices = HIGHEST_EDU_LEVEL_CHOICES,
    )
    marital_status_checkbox = forms.ChoiceField(
        choices = MARITAL_STATUS_CHOICES,
    )
    income_level_range = forms.CharField() # get the input directly from the user
    number_of_units = forms.ChoiceField(
        choices = NUMBER_OF_UNITS_CHOICES,    
    )
    ownership_type = forms.ChoiceField(
        choices = OWNERSHIP_TYPE_CHOICES,
    )
    number_of_rooms = forms.ChoiceField(
        choices = NUMBER_OF_ROOMS_CHOICES,    
    )
    building_age = forms.ChoiceField(
        choices = BUILDING_AGE_CHOICES,
    )
    price_range = forms.CharField() # get the input directly from the user
    number_of_vehicles_checkbox = forms.ChoiceField(
        choices = NUMBER_OF_VEHICLES_CHOICES,
    )
    commute_address = forms.CharField() # get the input directly from the user
    commute_type = forms.ChoiceField(
        choices = COMMUTE_TYPE_CHOICES,
    )
    commute_time_range = forms.CharField() # get the input directly from the user
    school_level = forms.ChoiceField(
        choices = SCHOOL_LEVEL_CHOICES,
    )
    school_quality_importance = forms.ChoiceField(
        choices = SCHOOL_QUALITY_CHOICES,
    )
    night_life_importance = forms.ChoiceField(
        choices = NIGHT_LIFE_CHOICES,
    )
    noise_level_checkbox = forms.ChoiceField(
        choices = NOISE_LEVEL_CHOICES,
    )
    crime_level_checkbox = forms.ChoiceField(
        choices = CRIME_LEVEL_CHOICES,
    )
    boroughs = forms.MultipleChoiceField(
        choices = BOROUGH_CHOICES,
    )















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






