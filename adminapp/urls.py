from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category', views.category, name='category'),
    path('feedback', views.feedback, name='feedback'),
    path('user', views.user, name='user'),
    path('payment', views.payment, name='payment'),
    path('subcategory', views.subcategory, name='subcategory'),
    path('staff', views.staff, name='staff'),
    path('product', views.product, name='product'),
    path('cart', views.cart, name='cart'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('orderreport', views.orderreport, name='orderreport'),
    path('pendingorder', views.pendingorder, name='pendingorder'),
    path('confirmorder', views.confirmorder, name='confirmorder'),
    path('completeorder', views.completeorder, name='completeorder'),
    path('cancelorder', views.cancelorder, name='cancelorder'),
    path('userreport', views.userreport, name='userreport'),
    path('feedbackreport', views.feedbackreport, name='feedbackreport'),
    path('paymentreport', views.paymentreport, name='paymentreport'),
    path('productreport', views.productreport, name='productreport'),
    path('categoryedit', views.categoryedit, name='categoryedit'),
    path('subcategoryedit', views.subcategoryedit, name='subcategoryedit'),
    path('staffedit', views.staffedit, name='staffedit'),
    
]
   