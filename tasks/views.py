from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from .forms import ProjectForm, TaskForm, UserRegisterForm

# Create your views here.




@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, "project_list.html", {"projects": projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    tasks = project.task_set.all()
    return render(request, "project_detail.html", {"project": project, "tasks": tasks})

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "project_form.html", {"form": form})

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = TaskForm()
    return render(request, "task_form.html", {"form": form})

@login_required
def completed_projects_report(request):
    projects = Project.objects.filter(owner=request.user, completed=True)
    return render(request, "completed_projects_report.html", {"projects": projects})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, project__owner=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("project_detail", pk=task.project.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, "task_detail.html", {"task": task, "form": form})







def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт для {username} успешно создан! Теперь вы можете войти.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
