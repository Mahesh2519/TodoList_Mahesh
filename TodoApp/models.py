from django.db import models
from datetime import date, datetime

# Create your models here.

class task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

	def __str__(self):
		return self.title

# class Task(models.Model):
#     first_name = models.CharField(max_length=50, null=False)
#     last_name = models.CharField(max_length=50)
#     TODO_LIST_CHOICE = (
#         ('book reading', 'book reading'),
#         ('pay_bill', 'pay_bill'),
#         ('watch_netflix', 'watch_netflix'),
#         ('grocery_shopping', 'grocery_shopping'),
#     )
#     todo_List = models.CharField(max_length=50, choices=TODO_LIST_CHOICE, null=False, blank=False)
#     completion_date = models.DateField("Complete on(mm/dd/2021)", auto_now_add=False, auto_now=False, blank=False, null=False)
#     timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
#
#     def __str__(self):
#         return self.name
