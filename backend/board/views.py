from django.shortcuts import render, redirect
from .forms import UserForm, VolunteerForm
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, FormView
from django.views import View
from .forms import VolunteerForm, UserLoginForm, SeniorForm
from django.http import HttpResponseRedirect
from .models import Volunteer, Senior
from django.contrib.auth.models import User

# Create your views here.
# seniors = [{
#     "content": "info",
#     "test": "super"
# }, {
#     "content": 'info2',
#     "test": "wow"
# },
#     {
#     "content": 'info3',
#     "test": "wow"
# },
#     {
#     "content": 'info4',
#     "test": "wow"
# },
#     {
#     "content": 'info5',
#     "test": "wow"
# },]


class IndexView(ListView):
    model=Volunteer
    template_name = "board/index.html"
    
    # volunteers= Volunteer.objects.all().order_by("first_name")
    # print(volunteers)

class RegisterView(View):
    def get(self, request):
        user_form = UserForm()
        volunteer_form = VolunteerForm()
        senior_form = SeniorForm()
        return render(request, 'board/register.html', {
            'user_form': user_form,
            'volunteer_form': volunteer_form,
            'senior_form': senior_form
        })
#  handlowanie dwoch rozny formow, ktory wykonwac kiedy

    def post(self, request):
        user_form = UserForm(request.POST)
        form_type = request.POST.get('form_type')
        print(form_type)
        if form_type == "senior_form":
            senior_form = SeniorForm(request.POST)
            if user_form.is_valid() and senior_form.is_valid():
                user = user_form.save(commit=False)
                user.email = user_form.cleaned_data['email']
                user.username = user_form.cleaned_data['email']
                user.set_password(user_form.cleaned_data['password'])
                user.save()

                senior = senior_form.save(commit=False)
                senior.user = user
                senior.save()
                senior_form.save_m2m()
                return redirect('main-page')
        else:
            volunteer_form = VolunteerForm(request.POST)
            print(request.POST)
            if user_form.is_valid() and volunteer_form.is_valid():
                # Tworzenie użytkownika
                user = user_form.save(commit=False)

                # Przypisanie adresu e-mail
                user.email = user_form.cleaned_data['email']
                user.username = user_form.cleaned_data['email']
                user.set_password(user_form.cleaned_data['password'])
                user.save()

                # Tworzenie profilu wolontariusza
                volunteer = volunteer_form.save(commit=False)
                volunteer.user = user
                volunteer.save()
                volunteer_form.save_m2m()

                return redirect('main-page')  # lub inny widok docelowy
        return render(request, 'board/register.html')


def login(req):
    return render(req, "board/login.html")

class LoginView(FormView):
    form_class = UserLoginForm
    template_name = "board/login2.html"
    success_url = "/index"
    def post(self, req):
        def form_invalid(self, form):
            response = super().form_invalid(form)
            return response
        def form_valid(self, form):
            print(User.check_password(req.POST["password"]))
            return HttpResponseRedirect("main-page")
        
def login2(req):
    return render(req, "board/login2.html")

def card(req):
    return render(req, "board/card.html", {
        "seniors": Senior.objects.all()
    })
