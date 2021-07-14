from django.shortcuts import render

#url for index page
def index(request):
    return render(request,'index.html',{})
#url for about page
def about(request):
    return render(request,'about.html',{})
