from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.

@api_view(['GET'])
def home(request):
    urls = [
        'list/',
        'detailedTodo/<int:id>',
        'createTodo/',
        'deleteTodo/<int:id>',
    ]
    return Response(urls)

@api_view(['GET'])
def listTodos(request):
    todos= Todo.objects.all()
    serialized = TodoSerializer(todos, many = True)
    return Response(serialized.data)

@api_view(['GET'])
def detailedTodo(request, id):
    todo = Todo.objects.get(id=id)
    serialized = TodoSerializer(todo)
    return Response(serialized.data)

@api_view(['POST'])
def createTodos(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateTodo(request, id):
    todo = Todo.objects.get(id=id)
    serializer = TodoSerializer(instance = todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return Response("Todo is deleted successfully")