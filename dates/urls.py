from django.conf.urls import include, url
from django.contrib import admin
from dates import views #gets all our view functions

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^about$', views.About.as_view(), name='about'),

    # url(r'^register$', views.User_Register.as_view(), name='register'),
    # url(r'^login$', views.User_Login.as_view(), name='login'),
    # url(r'^logout$', views.User_Logout.as_view(), name='logout'),

    # # here we send the url to the views with the slug id attached to it
    # url(r'^edit/(?P<dates_slug>[A-Za-z0-9\-\_]+)$', views.Edit_Date.as_view(), name="edit"),
    # url(r'^delete/(?P<dates_slug>[A-Za-z0-9\-\_]+)$', views.Delete_Date.as_view(), name='delete'),

    # url(r'^add$', views.AddDate.as_view(), name='add'),
    # url(r'^search$', views.SearchDate.as_view(), name='search'),
    # url(r'^area$', views.SearchDate_Area.as_view(), name='search_area'),
    # url(r'^results$', views.SearchDate.as_view(), name='results'),
    # url(r'^details/(?P<dates_slug>[A-Za-z0-9\-\_]+)$', views.DateDetails.as_view(), name='details'),
    # url(r'^price$', views.SearchDate_Price.as_view(), name='search_price'),
    # url(r'^top/(?P<dates_slug>[A-Za-z0-9\-\_]+)$', views.TopDate.as_view(), name='top'),
]
