from django.shortcuts import render,redirect
from .forms import ToDoForm
from.models import ToDoListData


def todohome(request):
    todo = ToDoListData.objects.all()

    form = ToDoForm()

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo:home')
    return render(request,'todo/home.html',{'form':form,'todo':todo})


    # if request.method =='POST':
    #     form = ToDoForm(request.POST)
    #     if form.is_valid():
    #         title = form.cleaned_data['title']
    #         todo =ToDoListData(title = title)
    #         todo.save()
    #         cd = form.cleaned_data
    #         print(title)
    #     else:
    #         return redirect('todo:home')
    # form = ToDoForm()
    # todo = ToDoListData.objects.all()
    # return render(request,'todo/home.html',{'form':form,'todo':todo})



def updateview(request, id):
    todo = ToDoListData.objects.get(id=id)
    form = ToDoForm(instance=todo)

    if request.method == 'POST':
        form = ToDoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
        return redirect('todo:home')


    return render(request,'todo/update.html',{'form':form})



def deleteview(request,id):
    todo = ToDoListData.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:home')
    return render(request,'todo/delete.html',{'todo':todo})










