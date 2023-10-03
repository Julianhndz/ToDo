from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, "task/index.html")


@login_required
def createTask(request):
    if request.method == "GET":
        return render(request, "task/create.html", {"form" : TaskForm()})
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            # Se guarda el formulario sin enviarlo a la base de datos utilizando el argumento "commit=False" dentro del .save para luego poder agregar el id del usuario a la tarea recien creada, luego se guarda en DB.
            new_task = form.save(commit=False)
            new_task.id_user = request.user
            new_task.save()
            return redirect("list")


@login_required
def listTask(request):
    # Se listan las tareas que estan en estado "pendiente" o "en progreso". Para esto se utiliza una consulta compleja, utilizando un Q object dentro del filter
    if request.user.is_authenticated:
        list_task = Task.objects.filter(Q(id_user=request.user, box_choices="Pendiente") | Q(id_user=request.user, box_choices="En progreso"))
    else:
        list_task = []
    return render(request, "task/list.html", {"tasks" : list_task})


@login_required
def completedList(request):
    if request.user.is_authenticated:
        completed = Task.objects.filter(id_user=request.user, box_choices="Completada")
    else:
        completed = []
    return render(request, "task/completed.html", {"completed":completed})


@login_required
def taskDetail(request, taskid):
    selectedTask = get_object_or_404(Task, pk=taskid, id_user=request.user)
    if request.method == "GET":
        form = TaskForm(instance=selectedTask)
        return render(request, "task/detail.html", {"task" : selectedTask,
                                                    "form" : form})
    else:
        try:
            form = TaskForm(request.POST, instance=selectedTask)
            if selectedTask.box_choices == "Completada":
                selectedTask.finished_date = timezone.now()
            form.save()
            return redirect("/list")
        except ValueError:
            return render(request, "task/detail.html", {"task" : selectedTask,
                                                        "form" : form,})


@login_required
def deleteTask(request, taskid):
    task = get_object_or_404(Task, pk=taskid, id_user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("/list")


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