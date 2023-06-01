from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginn,name='loginn'),
    path('new/',views.new,name='new'),
    path('form/',views.form,name='form'),
    path('final/',views.final,name='final'),
    path('redirect_idukki', views.redirect_idukki, name='redirect_idukki'),
    path('redirect_kottayam', views.redirect_kottayam, name='redirect_kottayam'),
    path('redirect_malappuram', views.redirect_malappuram, name='redirect_malappuram'),
    path('redirect_palakkad', views.redirect_palakkad, name='redirect_palakkad'),
    path('redirect_kochi', views.redirect_kochi, name='redirect_kochi'),

]