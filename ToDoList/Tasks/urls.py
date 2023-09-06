from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.createTask, name="create_task"),
    path("list/", views.listTask, name="list"),
    path("list/<int:taskid>/", views.taskDetail, name="taskDetail"),
    path("signup/", views.signUp, name="signup"),
    path("login/", views.log_in, name="login"),
    path("logout/", views.log_out, name="exit"),
]