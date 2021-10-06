from django.urls import path

app_name = 'TodoApp'

urlpatterns = [
    path('',views.HomeView.as_view(), name='home')
]
