from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'blog/index.html')

def about_us(request):
    return render(request,'blog/about us.html')

def projects(request):
    return render(request,'blog/projects.html')

def profile(request):
    return render(request,'blog/profile.html')