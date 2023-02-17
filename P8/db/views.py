from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("main/index.html")
    test = "mefaitplaisir"
    context = {
        'test1': test
    }
    return HttpResponse(template.render(context))
