from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Courses

def new(request):
    context = {
        'course': Courses.objects.all()
    }
    return render(request, 'new.html', context)

    

def create(request):
    errors = Courses.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Courses.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
        )
    return redirect('/')

def destroy(request, course_id):
    one_course = Courses.objects.get(id=course_id)
    context = {
        'course': one_course
    }
    return render(request, 'destroy.html', context)

def delete(request, course_id):
    to_delete =Courses.objects.get(id=course_id)
    to_delete.delete()
    return redirect('/')


