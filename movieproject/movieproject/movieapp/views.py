from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import movie
from . forms import movieform


def index(request):
   mov=movie.objects.all()
   context={
              'movie_list':mov
    }
   return render(request,'index.html',context)

def detail(request,movie_id):
    mov=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':mov})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        description=request.POST.get('description',)
        year=request.POST.get('year',)
        image=request.FILES['image']
        mov=movie(name=name,description=description,year=year,image=image)
        mov.save()
    return render(request,"add.html")

def update(request,id):
    mov=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form ,'movie':mov})

def delete(request,id):
    if request.method=='POST':
        mov=movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request,"delete.html")



