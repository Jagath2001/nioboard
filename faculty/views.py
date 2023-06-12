from django.shortcuts import render
from . import models
from .forms import InventoryFilterForm, FacultyFilterForm, StudentFilterForm
# Create your views here.


def inventory(request):
    # data = Inventory.objects.all()

    form = InventoryFilterForm(request.GET)
    inventory_items = models.Inventory.objects.all()
    for item in inventory_items:
        item.c = item.quantity - item.distributed
        item.save()

    if form.is_valid():
        subcategory = form.cleaned_data.get('category')
        stream_name = form.cleaned_data.get('stream')
        status_name = form.cleaned_data.get('status')


        if subcategory:
            inventory_items = inventory_items.filter(subcategory__name=subcategory)
        if stream_name:
            inventory_items = inventory_items.filter(stream__name=stream_name)
        if status_name:
            inventory_items = inventory_items.filter(status__name=status_name)


    context = {
            'form': form,
            'data': inventory_items,
        }

    return render(request,'products.html',context)




def Student(request):
    # data = Inventory.objects.all()

    form = StudentFilterForm(request.GET)

    student_items = models.Student.objects.all()

    if form.is_valid():
        Last_name = form.cleaned_data.get('Last_name')
        First_name = form.cleaned_data.get('First_name')
        Student_id = form.cleaned_data.get('Student_id')

        if Last_name:
            student_items = student_items.filter(Last_name=Last_name)
        if First_name:
            student_items = student_items.filter(First_name=First_name)
        if Student_id:
            student_items = student_items.filter(Student_id=Student_id)


    context = {
            'form': form,
            'data': student_items,
        }

    return render(request,'students.html',context)



def Faculty(request):
    # data = Inventory.objects.all()

    form = FacultyFilterForm(request.GET)

    faculty_items = models.Faculty.objects.all()

    if form.is_valid():
        Last_name = form.cleaned_data.get('Last_name')
        First_name = form.cleaned_data.get('First_name')
        Employee_id = form.cleaned_data.get('Employee_id')
        Employee_department = form.cleaned_data.get('Employee_department')

        if Last_name:
            faculty_items = faculty_items.filter(Last_name=Last_name)
        if First_name:
            faculty_items = faculty_items.filter(First_name=First_name)
        if Employee_id:
            faculty_items = faculty_items.filter(Employee_id=Employee_id)


    context = {
            'form': form,
            'data': faculty_items,
        }

    return render(request,'faculty.html',context)



def projects(request):

    data = models.Projects.objects.all()

    context = {
        'data':data
    }

    return render(request,'projects.html', context)