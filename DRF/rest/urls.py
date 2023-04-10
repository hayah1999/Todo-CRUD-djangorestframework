from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ),
    path('list/', views.listTodos),
    path('createTodo/', views.createTodos),
    path('detailedTodo/<int:id>/', views.detailedTodo),
    path('updateTodo/<int:id>/', views.updateTodo),
    path('deleteTodo/<int:id>', views.deleteTodo),
]