from django.urls import path
from todolist_app import views


urlpatterns = [
    path('',views.index,name='index'),
    path('update_done_status/<task_id>',views.update_done_status,name='update_done_status'),
    path('delete/<task_id>',views.delete_task,name ='delete_task'),
    path('edit/<task_id>',views.edit_task,name='edit_task'),
    path('todolist/',views.todolist,name='todolist'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
]
