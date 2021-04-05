from django.contrib import admin
from django.urls import path,include
from todolist_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todolist_app.urls')),
    path('account/',include('users_app.urls')),
]
