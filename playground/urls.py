from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.index,name='index'),
    path('todo_page/create/', views.create_todo_page, name='todo_page_create'),
    path('todo_page/<task_id>/', views.view_todo_page, name='todo_page_view'),
]