from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.homepage,name='homepage'),
    path("table",views.table,name='table'),
    path("form",views.form,name='form'),
    path("signup",views.signup,name='signup'),
    path("thankyou",views.thankyou,name='thankyou'),
    path("feedback",views.feedback,name='feedback'),
    path("landingpage",views.landingpage,name='landingpage'),
    path("coffeelover",views.coffeelover,name='coffeelover'),
    path("CLform",views.CLform,name='CLform'),
    path("js",views.js,name='js'),
    path("js1",views.js1,name='js1'),
    path("jquery",views.jquery,name='jquery'),

]
