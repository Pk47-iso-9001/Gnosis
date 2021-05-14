from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('physics', views.physics, name='physics'),
    path('chemistry', views.chemistry, name='chemistry'),
    path('mathematics', views.mathematics, name='mathematics'),
    path('computer', views.computer, name='computer'),
    path('biology', views.biology, name='biology'),
    path('english', views.english, name='english'),
    path('nepali', views.nepali, name='nepali'),
    path('question', views.question, name='question'),
    path('entertainment', views.entertainment, name='entertainment'),
    path('about', views.about, name='about'),
    path('question_physics', views.question_physics, name='question_physics'),
    path('question_mathematics', views.question_mathematics, name='question_mathematics'),
    path('question_computer', views.question_computer, name='question_computer'),

]