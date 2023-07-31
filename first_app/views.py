from django.shortcuts import render
from . forms import contactForm
# Create your views here.
def home(request):
    return render(request, './first_app/home.html', {"name" : "I am Rahim", "marks" : 86,"courses" : [
        {
        "id" : 1,
        "course" : "C",
        "teacher" : "Rahim"
        },
        {
        "id" : 2,
        "course" : "C++",
        "teacher" : "Kahim"
        },
        {
        "id" : 3,
        "course" : "Python",
        "teacher" : "Fahim"
        },
        ]})
    
def about(request):
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        select=request.POST.get('select')
        
        return render(request, './first_app/about.html', context={'name':name, 'email':email, 'select':select})
    else:
        return render(request, './first_app/about.html')
    


def submit_form(request):
    return render(request, './first_app/form.html')

def DjangoForm(request):
    form=contactForm(request.POST)
    if form.is_valid():
        print("form")
        print(form.cleaned_data)
    return render(request,'./first_app/django_form.html', {'form':form})