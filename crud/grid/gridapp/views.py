from django.shortcuts import get_object_or_404, redirect, render
from .models import Employer
from .forms import EmployerForm

# Create your views here.
def index(request):
    emp = Employer.objects.all()
    context = {
        'emp' : emp
    }
    return render(request, 'index.html', context=context)

def addnew(request):
    if request.method == "POST":
        form = EmployerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = EmployerForm()
        context = {
            'form': form
        }
    return render(request, 'add.html', context=context)


def edit(request, id):  
    employee = Employer.objects.get(id=id)
    context = {
        'employee': employee
    } 
    return render(request, 'edit.html', context=context)  


def update(request, id):  
    employee = Employer.objects.get(id=id)  
    form = EmployerForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'employee': employee})  


def delete(request, id):  
    employee = Employer.objects.get(id=id)  
    employee.delete()  
    return redirect("/")  