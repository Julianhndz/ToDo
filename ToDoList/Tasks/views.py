from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

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

@login_required
def listTask(request):
    if request.user.is_authenticated:
        list_task = Task.objects.filter(id_user=request.user)
    else:
        list_task = []
    return render(request, "task/list.html", {"tasks" : list_task})


def signUp(request):
    if request.method == "GET":
        return render(request, "registration/signup.html", {"form" : UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user_register = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user_register.save()
                login(request, user_register)
                return redirect("index")
            except IntegrityError:
                # Se maneja el error de que el nombre del usuario que se quiere crear sea igual a uno ya existente. Django hace la comparación de manera automatica, acá solamente mostramos un mensaje de error en pantalla.
                return render(request, "registration/signup.html", {"form": UserCreationForm,
                                                                   "error": "Usuario ya existe"})
        return render(request, "registration/signup.html", {"form": UserCreationForm,
                                                            "error": "Las contraseñas no coinciden."})


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