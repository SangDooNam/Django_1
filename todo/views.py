from django.shortcuts import render
from django.http import HttpResponse
from .models import todos
from django.urls import reverse

# Create your views here.

def todo(request, num):
    n = len(todos)
    
    for i in range(n):
        if num == i + 1:
            if num == 1:
                next_url = reverse('todo:todo', args=(num+1,))
                result = f"""
                        <h1>To Do number{num}</h1>
                        <h3>{todos[i]['topic']}</h3>
                        <p>{todos[i]['text']}</p>
                        <p>{todos[i]['status']}</p>
                        <a>Previous todo</a> | <a href={next_url}>Next todo</a>
                        """
            elif num == n:
                prev_url = reverse('todo:todo', args=(num-1,))
                result = f"""
                        <h1>To Do number{num}</h1>
                        <h3>{todos[i]['topic']}</h3>
                        <p>{todos[i]['text']}</p>
                        <p>{todos[i]['status']}</p>
                        <a href={prev_url}>Previous todo</a> | <a>Next todo</a>
                        """
            else:
                next_url = reverse('todo:todo', args=(num+1,))
                prev_url = reverse('todo:todo', args=(num-1,))
                result = f"""
                        <h1>To Do number{num}</h1>
                        <h3>{todos[i]['topic']}</h3>
                        <p>{todos[i]['text']}</p>
                        <p>{todos[i]['status']}</p>
                        <a href={prev_url}>Previous todo</a> | <a href={next_url}>Next todo</a>
                        """
            return HttpResponse(result)
        

