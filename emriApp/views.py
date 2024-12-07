from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required



def home(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    context = {"infoItems": items, "infoCategories": categories}
    return render(request, "home.html", context)

def about(request):
    categories = Category.objects.all()
    context = {"infoCategories": categories}
    return render(request, "about.html", context)

def detailItems(request, id):
    categories = Category.objects.all()
    detail = Item.objects.get(pk=id)
    context = {"detail":detail, "infoCategories": categories}
    return render(request, "detailItems.html", context)

def category(request, id):
    categories = Category.objects.all()
 
    detailCategory = Category.objects.get(pk=id)
    
    itemsCat = Item.objects.filter(item_category=detailCategory)
    context = {"detailCategory":detailCategory, 
               "infoCategories": categories,
               "itemsCat":itemsCat}
    return render(request, "categories.html", context)

def contact(request):
    categories = Category.objects.all()
    context = {"infoCategories": categories}
    if request.method == "POST":
        emri = request.POST["firstName"]
        mbiemri = request.POST["lastName"]
        email = request.POST["email"]
        koment = request.POST["comment"]
        if emri == "" and mbiemri == "" and email == "" and koment == "":
            messages.error(request, "Ploteso fushat")
        else:
            Contact(
                contact_name=emri,
                contact_surname=mbiemri,
                contact_email=email,
                contact_comment=koment,
            ).save()
            messages.success(request, "Faleminderit")
    return render(request, "contact.html", context)


def register(request):
    categories = Category.objects.all()
    context = {"cat": categories}
    
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
       
        if (
            first_name == ""
            and last_name == ""
            and username == ""
            and email == ""
            and password == ""
            and confirm_password == ""
        ):
            return redirect("../register/")
        else:
            
            if password == confirm_password:
                
                if User.objects.filter(username=username).exists():
                    
                    return redirect("/")
                else:
                    
                    user = User.objects.create_user(
                        email=email,
                        username=username,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.set_password(password)
                    
                    user.save()
                    
                    return redirect("../login/")
    else:
        return render(request, "auth/register.html", context)


def login(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
      
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
           
            auth.login(request, user)
            return redirect("/")
        else:
           
            return redirect("login/")
    else:
        return render(request, "auth/login.html", context)



def logout(request):
    
    auth.logout(request)
    return redirect("/")



@login_required(login_url="/login/")
def accessLogin(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "accessLogin.html", context)