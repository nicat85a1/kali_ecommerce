from django.urls import path
from user.views import register_view, login_view, logout_views

urlpatterns = [
    path("register", register_view, name="register_views"),
    path('login', login_view, name="login_views"),
    path("logout", logout_views, name="logout_views")
    ]
