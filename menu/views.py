from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from .models import Food, Weekly
import json

# Create your views here.

def index(request) :
    return render(request, "menu/index.html")

def base(request) :
    return render(request, "menu/hello.html")

class IndexClass(View) :
    def get(self, request):
        ketqua = "123"
        return HttpResponse(ketqua)

class LoginClass(View) :
    def get(self, request):
        if request.user.is_authenticated:
            return food_menu(request)
        else:
            return render(request, 'menu/login.html')
    def post(self, request):
        user_name = request.POST.get('user-name')
        pass_word = request.POST.get('pass-word')
        my_user = authenticate(request, username=user_name, password=pass_word)
        if my_user is None:
            return render(request, 'menu/login.html')
        else:
            login(request, my_user)
            foods = Food.objects.all()
            context = {'foods': foods}
            return render(request, 'menu/foodmenu.html', context)

class ViewUser(LoginRequiredMixin, View):
    login_url = '/menu/login/'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            username = form.cleaned_data.get('user-name')
            messages.success(request, f'Account created for {username} !')
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'menu/signup.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('login')

def food_menu(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        foods = Food.objects.all()
        context = {'foods': foods}
        return render(request, 'menu/foodmenu.html', context)

#@decorators.login_required(login_url='/menu/login/')
def food_card(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        foods = Food.objects.all().filter(food_id=id)
        return render(request, 'menu/foodcard.html', {'foods': foods})

def error(request):
    return render(request, 'menu/404.html')

class Profile(View):
    def get(self, request):
        if request.user.is_authenticated:
            current_user = request.user
            hello = "123"
            schedule = Weekly.objects.get(week_id=current_user)
            week = {
                'monday': schedule.monday,
                'tuesday': schedule.tuesday,
                'wednesday': schedule.wednesday,
                'thursday': schedule.thursday,
                'friday': schedule.friday,
                'saturday': schedule.saturday,
                'sunday': schedule.sunday,
            }

            foods = Food.objects.all()
            context = {'foods': foods, 'schedule': week}
            return render(request, 'menu/profile.html', context)
        else:
            return render(request, 'menu/login.html')


