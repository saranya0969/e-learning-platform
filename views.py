from django.shortcuts import render, redirect
from .models import Lesson, Contact

def home(request):
    lessons = Lesson.objects.all()
    return render(request, 'home.html', {'lessons': lessons})

def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        return redirect('home')
    return render(request, 'contact.html')
