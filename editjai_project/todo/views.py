from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.

def hello(request):
    text = "<h1> hello, this is jai</h1>"
    return HttpRespone(text)
def todoView(request):
    #return HttpResponse("hello , this is todo View"
    var = TodoItem.objects.all()
    return render(request, 'todo.html', {'all': var})
def addTodo(request):
    #creating a new todo item and save and redirecting the user to /todo
    var = request.POST['content']
    new_item = TodoItem(content = var)
    new_item.save()
    return HttpResponseRedirect('/todo/')
def deleteTodo(request, todo_id):
    var = TodoItem.objects.get(id = todo_id)
    var.delete()
    return HttpResponseRedirect('/todo/')
