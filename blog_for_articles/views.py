from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def  index(request):
     #return HttpResponse('hello')
     return render(request,'blog_for_articles/Blog.html')

def  admin(request):
     #return HttpResponse('hello')
     return render(request,'blog_for_articles/admin.html')

def  home(request):
     #return HttpResponse('hello')
     return render(request,'blog_for_articles/page.html')
