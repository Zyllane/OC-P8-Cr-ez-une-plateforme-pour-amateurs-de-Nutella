from django.shortcuts import render
from .forms import UserRegisterForm, UserLoginForm
from .models import User
import requests

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("main/index.html")
    test = "mefaitplaisir"
    context = {
        'test': test
    }
    return HttpResponse(template.render(context))

def user_register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    context={"form":form}
    return render(request,"user/user_register.html",context)

def user_login(request):
    form = UserLoginForm()
    context = {"form": form}
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user_exist = User.objects.filter(mail=request.POST['mail'], password=request.POST['password']).exists()
            if user_exist:
                response = render(request, "main/index.html", context)
                response.set_cookie("mail", request.POST["mail"])
                response.set_cookie("login", True)
                return response
    return render(request,"user/user_login.html",context)

def product_search(request):
    if request.method == "POST":
        url = "https://fr.openfoodfacts.org/data"