from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("", views.IndexView.as_view(), name="main-page"),
    path("register/", views.RegisterView.as_view(), name="register-page" ),
    path("about/", views.AboutUsView.as_view(), name="about-page"),
    path("services/", views.ServicesView.as_view(), name="service-page"),
    path("contact/", views.ContactView.as_view(), name="contact-page"),
    path("card/", views.card, name="card-page"),
    path("logout/", LogoutView.as_view(next_page="main-page"), name="logout-page")
    # path("login2/", views.LoginView.as_view())
]
