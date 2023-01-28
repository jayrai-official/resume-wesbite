from django.shortcuts import render
from core.models import Contact

# Create your views here.
def home(request):
    return render(request,'core/index.html',{'home':'active'})

def contact(request):
    if request.method=='POST':
        fetched_name = request.POST['name']
        fetched_email = request.POST['email']
        fetched_mob_no = request.POST['phone-no']
        fetched_msg = request.POST['msg']

        register = Contact(name=fetched_name,email=fetched_email,mob_no=fetched_mob_no,msg=fetched_msg)
        register.save()
        print("Data Saved sucessfully")

    return render(request,'core/contact.html',{'contact':'active'})