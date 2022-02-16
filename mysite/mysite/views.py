from curses.ascii import HT
import imp
from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service

def homePage(request):
    serviceData=Service.objects.all()
    #for a in serviceData:
        #print(a)
        #print(a.service_icon)
    data={
        'serviceData':serviceData
    }

    return render(request,"index.html",data)

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def form(request):
    total=0
    try:
        if request.method=="POST":
            n1=request.POST.get('num1')
            n2=request.POST.get('num2')
            total=n1+n2

    except:
        pass
    return render(request,"userForm.html",{'output':total})

def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=float(request.POST.get('num1'))
            n2=float(request.POST.get('num2'))
            opr=request.POST.get('opr')

            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2



    except:
        c="Invalid Operation.."
    print(c)
    return render(request,"calculator.html",{'c':c})

def oddeven(request):
    c=''
    if request.method=="POST":
        n=float(request.POST.get('num1'))
        if n%2==0:
            c="Even Number"
        else:
            c="Odd Number"
    return render(request,"oddeven.html",{'c':c})

def marksheet(request):
    if request.method=="POST":
        s1=float(request.POST.get('sub1'))
        s2=float(request.POST.get('sub2'))
        s3=float(request.POST.get('sub3'))
        s4=float(request.POST.get('sub4'))
        s5=float(request.POST.get('sub5'))
        t=s1+s2+s3+s4+s5
        p=t*100/500
        if p>=50:
            d="First Division"
        elif p>=48:
            d="Second Division"
        elif p>=30:
            d="Third Division"
        else:
            d="failed"
        data={
            'total':t,
            'per':p,
            'div':d
        }
        return render(request,"marksheet.html",data)
    return render(request,"marksheet.html")

def int(request,intId):
    return HttpResponse(intId)

def string(request,stringId):
    return HttpResponse(stringId)
    
def slug(request,slugId):
    return HttpResponse(slugId)


def test(request):
    data={
        'title':'Home page',
        'bbody': 'This is template from variable',
        'clist': ['PHP','Java','python'],
        'number':[1,2,3,4,5,6,7,8,9],
        'student_details':[
            {'name':'pradeep','phone':9823423},
            {'name':'bom','phone':9893820984}
        ]
    }
    return render(request,'test.html',data)