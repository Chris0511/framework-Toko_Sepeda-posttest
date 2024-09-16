from django.shortcuts import render

def homepage(request):
    return render(request,'toko/index.html')

def about(request):
    return render(request,'toko/about.html')