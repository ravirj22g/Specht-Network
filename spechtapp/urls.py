from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('login/', views.login_user, name = 'login_user'),
    path('logout/', views.logout_user, name = 'logout_user'),
    path('signup/', views.signup_user, name = 'signup_user'),


]