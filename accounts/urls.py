from django.urls import path
from . import views

urlpatterns = [
    path('',views.account_page, name = "account_page"),
    path('register',views.register, name = "register"),
    path('login', views.login, name = "login"),
    path('logout', views.logout, name = "logout")
]
