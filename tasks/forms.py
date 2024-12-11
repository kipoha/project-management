from django import forms
from .models import Project, Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "start_date", "end_date", "completed"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"})
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["project", "name", "description", "completed"]
        widgets = {
            "project": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "completed": forms.CheckboxInput(attrs={"class": "form-check-input"})
        }











class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
