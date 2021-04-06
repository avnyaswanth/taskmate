from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TasksList
from todolist_app.forms import Taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    msg = {
        'index_text' : 'Welcome to home page!!!',
    }
    return render(request,'index.html',msg)

@login_required
def todolist(request):
    if request.method == "POST":
        form = Taskform(request.POST or None)
        if form.is_valid():
            form.save(commit=False).owner = request.user
            form.save()
            messages.success(request,"New Task Added!!!")
            return redirect('todolist')
    else:
        all_tasks = TasksList.objects.filter(owner=request.user)
        paginator = Paginator(all_tasks,4)
        page = request.GET.get('page')
        all_tasks = paginator.get_page(page)

        return render(request,'todolist.html',{'all_tasks':all_tasks})
 
def contact(request):
    msg = {'contact_text':'Welcome to contact page!!!',}
    return render(request,'contact.html',msg)

def about(request):
    msg = {'about_text':'Welcome to about page!!!',}
    return render(request,'about.html',msg)

@login_required
def delete_task(request,task_id):
    task_obj = TasksList.objects.get(pk=task_id)
    if task_obj.owner == request.user:
        task_obj.delete()
    else:
        messages.error(request,'Access Denied!')
    return redirect('todolist')

@login_required
def edit_task(request,task_id):
    if request.method == "POST":
        task_obj = TasksList.objects.get(pk=task_id)
        form = Taskform(request.POST or None,instance=task_obj)
        if form.is_valid():
            form.save()
            messages.success(request,"Task edited!!")
            return redirect('todolist')
    else:
        task_obj = TasksList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})
    
@login_required
def update_done_status(request,task_id):
    task_obj = TasksList.objects.get(pk=task_id)
    if task_obj.owner == request.user:
        task_obj.done_status = not task_obj.done_status
        task_obj.save()
    else:
        messages.error(request,'Access Denied!')
    return redirect('todolist')