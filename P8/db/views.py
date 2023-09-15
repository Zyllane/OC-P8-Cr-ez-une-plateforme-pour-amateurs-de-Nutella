from django.shortcuts import render
from .forms import UserRegisterForm, UserLoginForm
from .models import User, Product, Bookmark

import requests

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    response = render(request, "main/index.html")
    return response

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
            queryset = User.objects.filter(mail=request.POST['mail'], password=request.POST['password'])
            user_exist = queryset.exists()
            if user_exist:
                user = queryset.get()
                response = render(request, "main/index.html", context)
                response.set_cookie("mail", request.POST["mail"])
                response.set_cookie("login", "True")
                response.set_cookie("id_user", user.id)
                return response
    return render(request,"user/user_login.html",context)

def search_product(request):
    query_name = request.GET.get('search_product', None)
    if query_name:
        results = Product.objects.filter(name__contains=query_name)
        context = {"results":results, "login":request.COOKIES.get("login")}

    if request.method == "POST":
        bookmark = Bookmark()
        bookmark.id_product = Product.objects.get(pk=request.POST["id"])
        bookmark.id_user = User.objects.get(pk=request.COOKIES.get("id_user"))
        bookmark.save()

    return render(request, 'product/search_product.html', context)