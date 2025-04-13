from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.template import loader
from .models import Datas



# Create your views here.

def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
         form.save()
         messages.success(request,"your account has been created and you can logged into inn now")
         return redirect ('login')
    else:
        form = UserRegistrationForm()
        
        
    context = {'form':form}
    return render(request,'register.html',context)
    
def index(request):
   return render(request,'index.html')



def about(request):
    msg = loader.get_template('about.html')
    return HttpResponse(msg.render())

def details(request):
    mydata=Datas.objects.all()
    if(mydata!=""):
        return render(request,"details.html",{"datas":mydata})
    else:
        return render(request,"details.html")  

def marriage(request):
    msg = loader.get_template('marriage.html')
    return HttpResponse(msg.render())  
     
def contactt(request):  
        return render(request,"contactt.html")
def story(request):  
        return render(request,"story.html")  
def services(request):  
        return render(request,"services.html") 
def traditional(request):  
        return render(request,"traditional.html") 
def destination(request):  
        return render(request,"destination.html") 
def reception(request):  
        return render(request,"reception.html") 
def pubberty(request):  
        return render(request,"pubberty.html") 
def birthday(request):
        return render(request,"birthday.html")
def logout(request):
        return render(request,"logout.html")
def admin_log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin123':
            messages.success(request, "Welcome, Admin!")
            return redirect('details')  # or any admin page
        else:
            messages.error(request, "Invalid admin credentials.")
    
    return render(request, 'admin_log.html')



def addData(request):
      if request.method=="POST":
        name=request.POST["name"]
        address=request.POST["address"]
        mobile=request.POST["mobile"]
        gender=request.POST["gender"]
        email=request.POST["email"]
        event=request.POST["event"]
       
        



        obj=Datas()
        obj.Name=name
        obj.Address=address
        obj.Mobile=mobile
        obj.Gender=gender
        obj.Email=email
        obj.Event=event
       
       
      
        obj.save()
        mydata=Datas.objects.all()
        return redirect("index")
      return render(request,"index.html")

def updateData(request,id):
        mydata=Datas.objects.get(id=id)
        if request.method=="POST":
          name=request.POST["name"]
          address=request.POST["address"]
          mobile=request.POST["mobile"]
          gender=request.POST["gender"]
          email=request.POST["email"]
          event=request.POST["event"]
          
        
          mydata.Name=name
          mydata.Address=address
          mydata.Mobile=mobile
          mydata.Gender=gender
          mydata.Email=email
          mydata.Event=event
         
          mydata.save()
          return redirect("index")
        return render(request,"update.html",{"data":mydata})
       
def deleteData(request,id):
    mydata=Datas.objects.get(id=id)
    mydata.delete()
    return redirect("index")



      
    
