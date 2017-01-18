from .models import Student
from django.shortcuts import render, get_object_or_404



# Create your views here.

def home(request):

    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'contact/home.html',context=context)

def detail(request,studentid):
    student = get_object_or_404(student,pk=studentid)

    context = {'student':student}
    return render(request, 'contact/details.html',context=context)
