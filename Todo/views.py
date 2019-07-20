from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
class TodoListView(LoginRequiredMixin,ListView):
    model = Todolist
    template_name = "index.html"
    login_url = 'login'

class TodoCreateView(CreateView):
    model = Todolist
    template_name = "make_list.html"
    fields = '__all__'

class TodoUpdateView(UpdateView):
    model = Todolist
    template_name = "update_list.html"
    fields = ('title',)

class TodoDeleteView(DeleteView):
    model = Todolist
    template_name = "delete_list.html"
    success_url = reverse_lazy ('home')

class TodoDetailView(DetailView):
    model = Todolist
    template_name = "list_detail.html"

