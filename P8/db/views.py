from django.shortcuts import render
from .forms import UserForm

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
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    context={"form":form}
    return render(request,"user/user_register.html",context)
