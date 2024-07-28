from django.shortcuts import render
from django.http import  HttpResponse
from django.template import loader
# Create your views here.

def home(request):

    

    template = loader.get_template("home.html")
    
    # return  HttpResponse("Home members ")
    # return render(request, "home.html")
    return HttpResponse(template.render())

def members(request):

    

    template = loader.get_template("all_members.html")

    return HttpResponse(template.render())