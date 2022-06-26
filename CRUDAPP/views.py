from readline import insert_text
from django.shortcuts import render, redirect
from CRUDAPP .models import Employee
from .models import Employee

# Create your views here
def insert_emp(request):
    if request == "POST":
        EmpId = request.POST['EmpId']
        EmpName = request.POST['EmpName']
        EmpGender = request.POST['EmpGender']
        EmpEmail = request.POST['EmpEmail']
        EmpDesignation = request.POST['EmpDesignation']
        data = Employee(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail, EmpDesignation=EmpDesignation)
        data.save()

        return redirect('show/')
    else:
        return render(request,'insert.html')

def show_emp(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employees':employees})

def edit_emp(request,pk):
    employees = Employee.objects.het(id=pk)
    if request.method =='POST':
        return redirect('/show')

    context = {
        'employees' : employees,
    }

    return render(request,'edit.html',context)


def remove_emp(request, pk):
    employees = Employee.objects.get(id=pk)

    if request.method =='POST':
        employees.delete()
        return redirect('/show')

    context = {
        'employees': employees,
    }
    return render(request, 'delete.html', context)

        

