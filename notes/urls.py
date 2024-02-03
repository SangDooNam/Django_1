from django.urls import path, re_path
from . import views

app_name = "notes"

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.new_home, name='new_home'),
    path('<int:num>/', views.number_notes, name='number_notes'),
    path('notes/<int:num>/',  views.new_number_notes, name= 'new_number_notes'),
    path('sections/', views.sections, name='sections'),
    path('notes/sections/',views.new_sections, name='new_sections'),
    re_path(r'^sections/(?P<subsection>[\w\d\W\D]+)/$', views.sub_sections, name='sub_sections'),
    re_path(r'^notes/sections/(?P<subsection>[\w\d\W\D]+)/$', views.new_sub_sections, name='new_sub_sections'),
    path('<str:query>/', views.web, name='web'),
    path('notes/<str:query>/', views.new_web, name='new_web'),
]


# urlpatterns = [
#     path('notes/', views.home, name='home'),
#     path('notes/<int:num>/', views.number_notes, name = 'number_notes'),
#     path('notes/sections/', views.sections, name='sections'),
#     re_path(r'notes/sections/(?P<subsection>[\w\d\W\D]+)/$', views.sub_sections, name='sub_sections'),
#     path('notes/<str:query>/', views.web, name='web'),
# ]



"""We now realize that some people had the notes bookmarked as http://localhost:8000/{id}/.

Your task is to create a new endpoint matching the previous pattern that redirects the user 

to the new URL at notes/{id}/.

You will have to point the path to a new view the does the redirection.

Additionally, refactor your code to use namespacing for each of the app views.

Once you are done, your website should look similar to this:"""