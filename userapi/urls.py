from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("hello-world/", views.hello_world, name="hello_world"),
    path("can-edit/", views.can_edit, name="can_edit"),
    path("retrieve-paints/", views.retrieve_paints, name="retrieve_paints"),
    path("update-paints", views.update_paints, name="update_paints"),
    path("login", views.login_function, name="login"),
    path("logout_user", views.logout_user, name="logout_user"),
]
