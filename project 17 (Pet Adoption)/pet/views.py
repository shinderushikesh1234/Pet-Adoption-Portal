from django.shortcuts import render,redirect
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import pet,petadopted
from django.contrib import messages
def home(request):
    return render(request,'home.html')
def registration(request):
    if request.method =='POST':
        First_Name = request.POST['Name']
        Email=request.POST['Email']
        username =request.POST['username']
        password =request.POST['password']
        confirmation_password =request.POST['cnfm_password']
        select_user=request.POST['select_user']
        if select_user == 'admin':
            select_user=True
        else :
            select_user=False
        if password == confirmation_password:
            user = User.objects.filter(username=username)
            if user:
                messages.error(request,'username already exist use different')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=Email,
                    first_name=First_Name,is_staff=select_user)
                user.save()
                messages.success(request,'created account successfully')
                return redirect('login')
        else:
            messages.error(request,'password should same password twice')
            return redirect('register')
    return render(request,'registration.html')
def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username ,password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('udashboard')
            else:
                return redirect('home')
        else:
            messages.error(request,'please check login details')
            return redirect('login')
    return render(request,'user.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def admin_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('udashboard')
            else:
                messages.error(request,"sorry you'r not admin/staff")
                return redirect('login')
        else:
           messages.error(request,'please check password | username')
           return redirect('Admin')
    return render(request,'admin.html')
def dashboard_view(request):
    search=None
    pets=pet.objects.filter(status='Available')
    Adopted=petadopted.objects.filter(user=request.user)
    if request.method=="POST":
        Breed=request.POST['breed']
        search=pet.objects.filter(Breed=Breed ,status='Available')
    return render(request,'user_dashboard.html',{'pets':pets,'search':search,'Adopted':Adopted})
def udashboard_view(request): 
    Users=User.objects.filter(is_active=True,is_staff=False,is_superuser=False)
    if request.method=='POST' and request.FILES['pet_image']:
        image=request.FILES['pet_image']
        Name=request.POST['pet_name']
        Location=request.POST['pet_location']
        Breed=request.POST['pet_breed']
        description=request.POST['pet_description']
        data=pet.objects.create(image=image,Name=Name,Location=Location,Breed=Breed,description=description)
        data.save()
        return redirect('udashboard')
    return render(request,'admin_dashboard.html',{'Users':Users})
def pet_adopt(request,pk):
    Pet=pet.objects.get(id=pk)
    if Pet.status=='Available':
        data=petadopted.objects.create(user=request.user,Pet=Pet)
        Pet.status='Adopted'
        Pet.save()
        data.save()
    else:
        message.error:'pet already adopted'
    return redirect('dashboard')