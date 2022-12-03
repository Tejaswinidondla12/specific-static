from django.shortcuts import render

# Create your views here.
def can(request):
    return render(request,'can.html')
