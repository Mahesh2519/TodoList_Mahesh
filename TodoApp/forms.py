from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}), label=False)
	due= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Due date...'}), label=False)

	class Meta:
		model = task
		fields = ['title', 'due']

class UpdateForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}))

	class Meta:
		model = task
		fields = ['title', 'due', 'complete']


# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = [first_name, last_name, todo_List, completion_date]

    # def clean_first_name(self):
    #     first_name = self.cleaned_data.get('first_name')
    #     if first_name == "" :
    #         raise forms.ValidationError("This field cannot be left blank ")
    #
    #
    # def clean_last_name(self):
    #     last_name = self.cleaned_data.get('last_name')
    #     if last_name == "" :
    #         raise forms.ValidationError("This field cannot be left blank ")


# class TaskSearchForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = [first_name, last_name]
