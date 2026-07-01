from django.shortcuts import render
from myapp.models  import Projects,Certifications
# Create your views here.
def base(request):
    return render(request,'Base.html')

def home(request):
    return render(request,'home.html')

def project(request):
    p=Projects.objects.all()
    ctx={'proj':p}
    return render(request,'projects.html',ctx)

def about_view(request):
    return render(request,'about.html')

def certificate_view(request):
    c=Certifications.objects.all()
    ct={'certify':c}
    return render(request,'certification.html',ct)

def contact(request):
    return render(request,'contact.html')