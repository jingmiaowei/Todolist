from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Todolist
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def TodoListView(request):
    all_todo_items = Todolist.objects.all()
    return render(request,'home.html',
            {'all_items': all_todo_items})

def addTodo(request):
    new_todo = Todolist(content = request.POST['title'])
    new_todo.save()
    return HttpResponseRedirect('/home/')

def TodoDelete(request,Todolist_id):
    delete_todo = Todolist.objects.get(id=Todolist_id)
    delete_todo.delete()
    return HttpResponseRedirect('/home/')

def TodoEdit(request):
    return render(request,'edit.html') 
 
 
def NewEdit(request,Todolist_id):
    if request.method == 'POST':
        new_todo = Todolist(content = request.POST['title'])
        new_todo.title = request.POST['edited']
        new_todo.save()
        return redirect("home")
    elif request.method == 'GET':
        content1 = {'needadd': Todolist.objects.get(id=Todolist_id).title }
        return render(request,'newedit.html',content1)  

def Finish(request, id): 
    if request.POST['status'] == 'finished':
        a= Todolist.objects.get(id=id)
        a.finish = True
        a.save()
        return redirect ("finish.html")
    else:
        a = Todolist.objects.get(id=id)
        a.finish = False
        a.save()
        return redirect ("finish.html")
