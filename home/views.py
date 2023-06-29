from django.shortcuts import render,redirect,HttpResponse
from home.models import Form
 



# Create your views here.

 


def homepage(request):
    return render (request,'base.html')

def table(request):
    return render (request,'table.html')

def form(request):
    return render (request,'form.html')

def thankyou(request):
    return render (request,'thankyou.html')

def signup(request):
    return render (request,'signup.html')

def feedback(request):
    return render (request,'feedback.html')

def landingpage(request):
    return render (request,'landingpage.html')

def coffeelover(request):
    return render (request,'coffeelover.html')

def CLform(request):
    return render (request,'CLform.html')

   
def js(request):
    return render (request,'js.html')

def js1(request):
    return render (request,'js1.html')

def jquery(request):
    return render (request,'jquery.html')




def Form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password= request.POST.get('password')
        # phone = request.POST.get('phone')
        # desc = request.POST.get('desc')
        # contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your Request has been Saved!')



    return render (request,'form.html')
    #return HttpResponse("This is Contact Page")

    