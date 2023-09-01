from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.createTask, name="create_task"),
    path("signup/", views.signUp, name="signup"),
    path("login/", views.log_in, name="login"),
    path("logout/", views.log_out, name="exit"),
]