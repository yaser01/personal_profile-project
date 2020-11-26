from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Project

def handler404(request,exception=None):
    print (exception)
    return HttpResponseRedirect("/404.html")
def page_404(request):
    return render('portfolio/404.html',template_name='portfolio/404.html')
def home(request):
    projects=Project.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects[1:],'firstproject':projects[0],'range': range(1,len(projects))})

