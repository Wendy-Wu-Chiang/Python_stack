from django.shortcuts import render, redirect

def index(request):
    return render(request, 'form.html')

def result(request):
    if request.method == 'POST':
        context={
            'name': request.POST['name'],
            'location': request.POST['location'],
            'language': request.POST['language'],
            'common': request.POST['common']
        }
        return render(request, 'result.html', context)
    return render(request, 'result.html')

def goback(request):
    if request.method == "GET":
        return redirect("/")

    
