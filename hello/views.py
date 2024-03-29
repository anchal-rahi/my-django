from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as lg
from django.contrib.auth.decorators import login_required


# Create your views here.
from hello.models import contact
def home(request):
   
   return render(request,"home.html")

def about(request):
    return render (request,"aboutus.html")

@login_required
def contactx(request):
    return render(request,"contact.html")


@login_required
def servicex(request):
    #orm
    mydata =contact.objects.all()
    context={"records" : mydata}
    
    return render(request,"services.html",context)

def nav(request):
    return render(request,"navbar.html")


def savethis(request):
    if request.method=="POST":
        Name=request.POST.get("name")
        Email=request.POST.get("email")
        Phonenumber=request.POST.get("number")
        message=request.POST.get("message")
        print(Name, Email)
        myimg = request.FILES.get('imgs')

        myemailmessage = f""""
        this is user contact us form data

        username={Name}
        useremail={Email}
        phonenumber={Phonenumber}
        message={message}

        
        THANK YOU :)
        """

        # mail=EmailMessage("this  email comming from django","this is me ","anchalrahi0@gmail.com",["kirtidhiman799@gmail.com"])
        # mail.send()

        mydata=contact(username=Name,useremail=Email,phonenumber=Phonenumber,message=message,myimage = myimg)
        mydata.save()

        messages.success(request,  "Data Saved Sucessfully...!")

        return redirect("services")


def deletedata(request,myid):
    # data=contact.objects.all()
    data=contact.objects.get(id=myid)
    data.delete()
    return redirect("services")


def updatethisdataok(request,myid):
    data=contact.objects.get(id=myid)
    return render(request,"contactupdate.html",{"yourdata":data})


def updatenow(request,update):
      if request.method=="POST":
        Name=request.POST.get("name")
        Email=request.POST.get("email")
        Phonenumber=request.POST.get("number")
        message=request.POST.get("message")
        img = request.FILES.get('imgx')

        mydata=contact.objects.get(id=update)
        mydata.username=Name
        mydata.useremail=Email
        mydata.phonenumber=Phonenumber
        mydata.message=message
        mydata.myimage = img
        mydata.save()

      return redirect ("services")

def searchthisdata (request):
    xyz=request.GET['query']
    searchdata=contact.objects.filter(username=xyz) 

    context={"records":searchdata}
    return render(request,"services.html",context)

def signpage(request):
    return render(request, "sign.html")

def signup(request):
   
    if request.method == "POST":
        username = request.POST.get("Username")
        email = request.POST.get("email")
        Password = request.POST.get("password")
        FullName = request.POST.get("Fullname")
        cpassword = request.POST.get("cpassword")

        if Password != cpassword:
            messages.warning(request, "password doesn't match")
            return redirect("signup")
        
        else:
            saveuser = User.objects.create_user(username = username, email = email, password=Password, first_name = FullName)
            saveuser.save()

            messages.success(request, "User Added Sucessfulyy.....!")
            return redirect("signup")
        
        # else:
        #     messages.warning(request, "password does not match!")

        #     return redirect("signup")
        


def logins(request):
    return render(request,"log.html")

def loginup(request):
       if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
    
        usercheck = authenticate(username=name, password=password)  

        if usercheck is not None:
            lg(request, usercheck)
            
            messages.success(request, "Login Sucessfully done..!")
            return redirect ("services")
        
        else:
            messages.warning(request, "PLease Enter vaild Crentationals! ")
            return redirect("login")
            

def logouthere(request):
    logout(request)
    return redirect("login")
     


     




