from django.shortcuts import render
from django.http import HttpResponse
from .models import notes
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
def home(request):
    return redirect('notes:new_home')
    
def new_home(request):
    return HttpResponse('''<h2>Welcome to my course notes!</h2>
                        <a href='/sections/'>Check the list of sections</a> |  
                        <a href='/1'>Read my first note</a>''')


def sections(requset):
    return redirect('notes:new_sections')


def new_sections(request):
    return HttpResponse('''<h3>Browse my notes by section</h3>
                        <ol><li><a href='/sections/web_frameworks/'>Web Frameworks</a></li>
                        <li><a href='/sections/setting_up_django/'>Setting up Django</a></li>
                        <li><a href='/sections/url_mapping/'>URL Mapping</a></li></ol>
                        <a href='/'>Back to home</a>''')


def sub_sections(request,subsection):
    if subsection == 'web_frameworks':
        return redirect('notes:new_sub_sections', subsection)
    elif subsection == 'setting_up_django':
        return redirect('notes:new_sub_sections', subsection)
    elif subsection == 'url_mapping':
        return redirect('notes:new_sub_sections', subsection)


def new_sub_sections(request,subsection):
    if subsection == 'web_frameworks':
        return web_frameworks(request)
    elif subsection == 'setting_up_django':
        return setting_up_django(request)
    elif subsection == 'url_mapping':
        return url_mapping(request)


def web_frameworks(request):
    lst = [note for note in notes if note['section'] == 'Web Frameworks']
            
    return HttpResponse(f"""
                        <h3>Note about {lst[0]['section']}</h3>
                        <ol><li>{lst[0]['text']}</li><li>{lst[1]['text']}</li><li>{lst[2]['text']}</li></ol>
                        <a href='/sections/'>Back to sections</a>
                        """)


def setting_up_django(request):
    lst = [note for note in notes if note['section'] == 'Setting up Django']
    return HttpResponse(f"""
                        <h3>Note about {lst[0]['section']}</h3>
                        <ol><li>{lst[0]['text']}</li><li>{lst[1]['text']}</li><li>{lst[2]['text']}</li></ol>
                        <a href='/sections/'>Back to sections</a>
                        """)


def url_mapping(request):
    lst = [note for note in notes if note['section'] == 'URL Mapping']
    
    return HttpResponse(f"""
                        <h3>Note about {lst[0]['section']}</h3>
                        <ol><li>{lst[0]['text']}</li><li>{lst[1]['text']}</li><li>{lst[2]['text']}</li></ol>
                        <a href='/sections/'>Back to sections</a>
                        """)

def web(request, query):
    return redirect('notes:new_web', query)


def new_web(request, query):
    lst = [note['text'] for note in notes if query in note['text'].lower()]
    
    if lst:
        lst_template = ''.join(f'<li>{note}</li>' for note in lst)
        result = f"<h3>Note matching {query}</h3> <ol>{lst_template}</ol> <a href='/sections/'>Back to sections</a>"
    else:
        result = "<h3>No matching notes found</h3>  <a href='/'>Back to home</a>"
    
    return HttpResponse(result)

def number_notes(request, num):
    return redirect('notes:new_number_notes', num)

def new_number_notes(request, num):
    n = len(notes)
    for i in range(n):
        if num == i + 1:
            if num == 1:
                next_url = reverse('notes:number_notes', args=(num+1,))
                result= f"""
                        <h1>Note number {num}</h1>
                        <h3>{notes[i]['section']}</h3>
                        <p>{notes[i]['text']}</p>
                        <a>Previous note</a> | <a href='/'>Back to home</a> | <a href='{next_url}'>Next note</a>
                        """
            elif num == n:
                prev_url = reverse('notes:number_notes', args=(num-1,))
                result= f"""
                        <h1>Note number {num}</h1>
                        <h3>{notes[i]['section']}</h3>
                        <p>{notes[i]['text']}</p>
                        <a href='{prev_url}'>Previous note</a> | <a href='/'>Back to home</a> | <a>Previous note</a>
                        """
            
            else:
                next_url = reverse('notes:number_notes', args=(num+1,))
                prev_url = reverse('notes:number_notes', args=(num-1,))
                result= f"""
                        <h1>Note number {num}</h1>
                        <h3>{notes[i]['section']}</h3>
                        <p>{notes[i]['text']}</p>
                        <a href='{prev_url}'>Previous note</a> | <a href='/'>Back to home</a> | <a href='{next_url}'>Next note</a>
                        """
            return HttpResponse(result)
