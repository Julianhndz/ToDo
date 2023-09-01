from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    return render(request, "task/index.html")


@login_required
def createTask(request):
    if request.method == "GET":
        return render(request, "task/create.html", {"form" : TaskForm()})
    else:
        # new_task = Task.objects.create(title=request.POST["title"], task_description=request.POST["task_description"], limit_date=request.POST["limit_date"], box_choices=request.POST["box_choices"])
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.id_user = request.user
            new_task.save()
            return redirect("index")
    

def log_in(request):
    if request.method == "GET":
        return render(request, "registration/login.html", {"form" : AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "registration/login.html", {"form" : AuthenticationForm,
                                                       "error" : "Username or password do not match, please verify."})
        return redirect("index")
    

def log_out(request):
    logout(request)
    return redirect("index")