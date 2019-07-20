from django.urls import path

from . import views

urlpatterns = [
    path('', TodoListView.as_view(), name='home'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='list_detail'),
    path('todo/new/', TodoCreateView.as_view(), name='make_list'),
    path('todo/edit/<int:pk>', TodoUpdateView.as_view(), name='update_list'),
    path('todo/delete/<int:pk>', TodoDeleteView.as_view(), name='delete_list'),
]