from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("add_contact", views.add_contact_view, name="add_contact"),
    path("search_users", views.search_users_view, name="search_users")
]