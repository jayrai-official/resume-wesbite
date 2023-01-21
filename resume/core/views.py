from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/index.html',{'home':'active'})

def contact(request):
    return render(request,'core/contact.html',{'contact':'active'})