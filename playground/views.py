from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
import datetime

# Create your views here.
#request -> response 
#request handler

def index(request):
    #Connect to the database
    all_todo_lists = Todo.objects.all()
    html = ''
    for task in all_todo_lists:
        url = '/index/todo_page/'+str(task.id)+'/'
        html+= '<a href="'+ url +'">Todo-List_'+ str(task.id) +'</a><br>'
    return HttpResponse(html)

def create_todo_page(request):
    if request.method == 'POST':
        task_txt = request.POST.get('task_Txt')
        date_created = request.POST.get('date')

        if task_txt:
            new_Task = Todo(task_Text=task_txt, date_created=date_created, isDone=False)
            new_Task.save()

    all_tasks = Todo.objects.all() 
    return render(request, 'create_Todo-List.html',{'all_tasks': all_tasks})    




def view_todo_page(request,task_id):
    #Connect to the database
    task_id_text = Todo.objects.get(id=task_id).task_Text
    return render(request, 'view_Todo-List.html', {'task_id': str(task_id), 'task_Text': task_id_text})

    #     form = TodoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    # else:
    #     form = TodoForm(initial={'date_created': datetime.date.today()})  # Set the initial date

    # try:
    #     form = request.POST['task_Text','date_created','done',]
    #     return ''
    # except ():
    #     return ''
    # else:


    #     something.save()
        #Connect to the database