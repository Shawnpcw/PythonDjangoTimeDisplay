from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
  # the index function is called when root is visited

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }

    print(context)
    return render(request, 'time_display/index.html',context)
