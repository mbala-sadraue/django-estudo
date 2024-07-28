from django.shortcuts import render
from django.http import  HttpResponse
from django.template import loader,Context
from members.models import Member
# Create your views here.

def home(request):

    template = loader.get_template("home.html")
    
    # return  HttpResponse("Home members ")
    # return render(request, "home.html")
    return HttpResponse(template.render())

def members(request):

    template = loader.get_template("all_members.html")
    

    members_list = Member.objects.all().values()
    context  = {"members":members_list}
    # print(members_list)
    return HttpResponse(template.render(context,request))

def details(request, id):

    template = loader.get_template("details.html")
    member = Member.objects.get(id= id)
    
    context = {"member":member}
    return HttpResponse(template.render(context, request))