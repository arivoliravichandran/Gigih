from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


# List all todos
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todo/todo_list.html", {"todos": todos})


# Add a new todo
def add_todo(request):
    if request.method == "POST":
        description = request.POST.get("description")
        Todo.objects.create(description=description)
        return redirect("todo_list")
    return render(request, "todo/add_todo.html")


# Update an existing todo
def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        todo.description = request.POST.get("description")
        todo.completed = "completed" in request.POST
        todo.save()
        return redirect("todo_list")
    return render(request, "todo/update_todo.html", {"todo": todo})


# Delete a todo
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("todo_list")
