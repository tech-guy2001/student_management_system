from django.shortcuts import render
from .models import MyMod

from django.contrib import messages 
from database_template import settings
from django.core.mail import send_mail
from django.core.mail  import EmailMessage
from database_template.settings import EMAIL_HOST_USER

# Create your views here.
def home(request):
    if request.method=='POST':
        roll_no=request.POST.get('rollno')
        name=request.POST.get('name')

        age=request.POST.get('age')
        course=request.POST.get('course')
        number=request.POST.get('phone_number')
        address=request.POST.get('address')
        email=request.POST.get('email')
        subject="nandha"
        message="this is nandha"
        
        ot_list=[email]
        send_mail(subject,message,EMAIL_HOST_USER,ot_list,fail_silently=True)
        MyMod.objects.create( rollno=roll_no,name=name,age=age,course=course,phone_number=number,address=address,email=email)
        messages.success(request, 'This is a success message.')
        message = 'This is a success .'  
        return render(request, 'home.html', {'message': message})
   
    
    return render(request,'home.html')

def showall(request):
    all=MyMod.objects.all()
    return render(request,"home.html",{'all':all})

def find(request):
   
    if request.method=="POST":
        select=request.POST.get("select")
        find_value=request.POST.get("find_value")
        if select=="by name":
            search=MyMod.objects.filter(name=find_value).values()
        elif select=="by rollno":
            search=MyMod.objects.filter(rollno=find_value).values()
        elif select=="by subject":
            search=MyMod.objects.filter(course=find_value).values()
        elif select=="by batch":
            search=MyMod.objects.filter(batch=find_value).values()
        elif select=="by qulification":
            search=MyMod.objects.filter(qulification=find_value).values() 
            
        return render(request,"search.html" ,{"search":search})
    return render(request,"search.html")

def search(request):


    return render(request,'search.html')
   
        
        
def find_like(request):
    s=""
    if request.method=="POST":
        selects=request.POST.get("selects")
        find_values=request.POST.get("find_values")
        if selects=="by first_name":
            s=MyMod.objects.filter(firstname=find_values).values()
        elif selects=="by last_name":
            s=MyMod.objects.filter(lastname=find_values).values()
        elif selects=="first_letter":
            s=MyMod.objects.filter(name__startswith=find_values).values()
       
            
        return render(request,"search.html" ,{"search":s})

    return render(request,"search.html")   
def contact(request):
    return render(request,'contact.html')