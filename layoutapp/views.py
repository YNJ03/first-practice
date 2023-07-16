from django.shortcuts import render
def Index(request) :
    return render(request, "layoutapp/index.html", {})

# Create your views here.
