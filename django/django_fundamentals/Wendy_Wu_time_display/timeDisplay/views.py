from django.shortcuts import render
from time import gmtime, strftime
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%m %p", gmtime())
    }
    return render(request, 'index.html', context)

