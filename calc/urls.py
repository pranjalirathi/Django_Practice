from django.urls import path

from . import views

'''-----Making a list of urlpatterns to provide mapping. These patterns tell Django how to route incoming web requests------'''
'''will call the function in views module where function is named as home'''
urlpatterns = [
    path('', views.home, name='patanahi'),
    path('add', views.add, name='add')
]
