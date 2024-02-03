from django.urls import path
from . import views

app_name = 'todo'



urlpatterns = [
    path('<int:num>/', views.todo, name='todo'),
    
]



