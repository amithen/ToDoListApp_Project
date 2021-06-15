from django import forms
from .models import ToDoListData

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoListData
        fields = "__all__"
