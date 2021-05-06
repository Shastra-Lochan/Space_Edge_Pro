from django.shortcuts import render, HttpResponse

# Create your views here.
def default(request):
    return render(request, 'index.html')

def index(request):
    return render(request,'Home.html')
    #return HttpResponse('Welcome To Space Edge Pro')

def about(request):
    return render(request, 'Topic_Description.html')
    #return HttpResponse("This is about")

def founders(request):
    return render(request, 'Members.html')
    #return HttpResponse("The Founders")

def contact(request):
    return render(request, 'Contact.html')
    #return HttpResponse("Contact Page")

def Index(request):
    return render(request, 'index.html')