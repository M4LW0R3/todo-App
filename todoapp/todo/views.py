from django.shortcuts import render
from django.http import HttpResponseRedirect
from todo.models import todoItem


# Create your views here.


def todoView(request):
    all_to_do_items = todoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_to_do_items})



def addTodo(request):
    new_item = todoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

    # create a new todoall_items
    # save
    # redirect the browser to '/todo/'

def deleteTodo(request, todo_id):
    item_to_delete = todoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')

