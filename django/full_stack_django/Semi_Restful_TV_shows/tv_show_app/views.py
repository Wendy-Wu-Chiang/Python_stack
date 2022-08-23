from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show


def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)


def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            released_date=request.POST['released_date'],
            description=request.POST['description']
        )
    return redirect('/shows')



def delete(request, show_id):
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/shows')


def update(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        to_update = Show.objects.get(id=show_id)
        to_update.title = request.POST['title']
        to_update.network = request.POST['network']
        to_update.released_date = request.POST['released_date']
        to_update.description = request.POST['description']
        to_update.save()

    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)


def new(request):
    return render(request, 'new.html')


def show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'show.html', context)


def edit(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'edit.html', context)
