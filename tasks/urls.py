from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("project/<int:pk>/", views.project_detail, name="project_detail"),
    path("project/new/", views.create_project, name="create_project"),
    path("task/new/", views.create_task, name="create_task"),
    path("task/<int:pk>/", views.task_detail, name="task_detail"),
    path("completed-projects/", views.completed_projects_report, name="completed_projects_report"),
    
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
