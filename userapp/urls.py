from django.urls import path

from . import views

urlpatterns = [
    path('', views.uindex, name='uindex'),
    path('uabout', views.uabout, name='uabout'),
    path('ucontact', views.ucontact, name='ucontact'),
    path('usignup', views.usignup, name='usignup'),
    path('usignin', views.usignin, name='usignin'),
    path('usignout', views.usignout, name='usignout'),
    path('uprofile', views.uprofile, name='uprofile'),
    path('uproduct', views.uproduct, name='uproduct'),
    path('uforgotpassword', views.uforgotpassword, name='uforgotpassword'),
    path('uterms', views.uterms, name='uterms'),
    path('uproductdetails', views.uproductdetails, name='uproductdetails'),   
    path('ucart', views.ucart, name='ucart'), 
    path('uorder', views.uorder, name='uorder'), 
    path('uorderdetails', views.uorderdetails, name='uorderdetails'), 
    path('upayment', views.upayment, name='upayment'),
    path('thank-you/', views.uthankyou, name='uthankyou'), 
   

]
   