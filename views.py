from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from .forms import PersonForm


def hello(request):
    return HttpResponse("hello, world")


def helloparams(request, param):
    return HttpResponse("param value: {0}".format(param))


def index(request):
    return render(request, "index.html")


def people(request):
    form = PersonForm()

    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            p = Person()
            p.first_name = form.cleaned_data["first_name"]
            p.last_name = form.cleaned_data["last_name"]
            p.age = form.cleaned_data["age"]
            p.save()
        else:
            form = PersonForm()

    po = Person.objects.all()
    return render(request, "people.html", {"people": po, "form": form})
