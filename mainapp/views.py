from django.shortcuts import render
from . import  models
from . models import student
from . models import mark
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def Index(request):
   return render(request, 'index.html',{})

def WhatsappData(Ph,Message):
    import time
    import webbrowser as web
    import pyautogui as pg
    Phone = "+91" +Ph
    web.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+Message)
    time.sleep(30)
    pg.press('enter')



def senddata(request):
    if request.method == "POST":
        Ph = request.POST['Phone']
        Message = request.POST['message']
        #print(ph,Message)
        WhatsappData(Ph,Message)
        msg="Message has successfully sent.."
        return render(request,"index.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found :) </h1>")

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def online(request):
    return render(request, 'online.html')

def one(request):
    return render(request, 'one.html')

def one2(request):
    return render(request, 'one2.html')

def one3(request):
    return render(request, 'one3.html')

def one4(request):
    return render(request, 'one4.html')

def one5(request):
    return render(request, 'one5.html')

def quiz(request):
    return render(request, 'quiz.html')

def reg_done(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
      #  phone = request.POST['phone']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        if password == repeat_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return render (request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return render (request, 'register.html')
            
            else:
                user = User.objects.create_user(username = username, email = email, password=password)
                user.save();
                print('user created')
               # return render (request, 'register.html')
        else:
            messages.info(request, 'password not matching...')
            return render (request, 'register.html')
        
        return render(request, 'reg_done.html')

    else:
        return render (request, 'register.html')

def log_done(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'log_done.html')

        else:
            return render(request, 'sorry.html')


    else:
        return render(request, 'sorry.html')

def home(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('rno') and request.POST.get('dob'):
            saverecord=student()
            saverecord.name=request.POST.get('name')
            saverecord.rno=request.POST.get('rno')
            saverecord.dob=request.POST.get('dob')
            saverecord.save()
            messages.success(request, 'Done Successfully...')
    return render (request, 'home.html')
