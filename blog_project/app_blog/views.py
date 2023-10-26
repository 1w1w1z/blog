from django.shortcuts import render

# Create your views here.
def Post(request):
    return render(request,'index.html')
    
