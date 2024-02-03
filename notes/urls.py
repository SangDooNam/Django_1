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

