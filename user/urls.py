from django.urls import path
from user.views import register_view

urlpatterns = [
    path("register", register_view, name="register_views")
    ]
