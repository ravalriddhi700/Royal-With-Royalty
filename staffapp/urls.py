from django.urls import path

from . import views

urlpatterns = [
    path('', views.sindex, name='sindex'),
    path('scategory', views.scategory, name='scategory'),
    path('sfeedback', views.sfeedback, name='sfeedback'),
    path('suser', views.suser, name='suser'),
    path('spayment', views.spayment, name='spayment'),
    path('ssubcategory', views.ssubcategory, name='ssubcategory'),
    path('sstaff', views.sstaff, name='sstaff'),
    path('sproduct', views.sproduct, name='sproduct'),
    path('scart', views.scart, name='scart'),
    path('slogin', views.slogin, name='slogin'),
    path('slogout', views.slogout, name='slogout'),
    path('sorderreport', views.sorderreport, name='sorderreport'),
    path('spendingorder', views.spendingorder, name='spendingorder'),
    path('sconfirmorder', views.sconfirmorder, name='sconfirmorder'),
    path('scompleteorder', views.scompleteorder, name='scompleteorder'),
    path('scancelorder', views.scancelorder, name='scancelorder'),
    
    
    path('spaymentreport', views.spaymentreport, name='spaymentreport'),
    
    path('scategoryedit', views.scategoryedit, name='scategoryedit'),
    path('ssubcategoryedit', views.ssubcategoryedit, name='ssubcategoryedit'),
    path('sstaffedit', views.sstaffedit, name='sstaffedit'),
    path('sprofile', views.sprofile, name='sprofile'),
    path('sproductedit', views.sproductedit, name='sproductedit'),
    
]
   