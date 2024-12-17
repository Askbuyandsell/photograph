from django.http import HttpResponse
from contact.models import Contact


from django.shortcuts import render
def home(request):
    return render(request, "index.html")
def portfolio(request):
    return render(request, "portfolio.html")
def gallery(request):
    return render(request, "gallery.html")
def experience(request):
    return render(request, "experience.html")
def contact(request):
    return render(request, "contact.html")


def form(request):
    n=''
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        
        
        info=Contact(name=name, email=email, phone=phone, message=message)
        info.save()
        n='data inserted'
        
    return render(request,"contact.html",{'n':n})