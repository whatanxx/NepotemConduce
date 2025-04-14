from django.urls import path
from . import views
urlpatterns = [
    path("", views.IndexView.as_view(), name="main-page"),
    path("register/", views.RegisterView.as_view(), name="register-page" ),
    path("login/", views.login, name="login-page"),
    path("card/", views.card, name="card-page"),
    path("login2/", views.LoginView.as_view())
]
