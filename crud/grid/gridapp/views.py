from django.shortcuts import redirect, render
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