from django.shortcuts import render
from manager.models import Manager
from login.models import Login
# Create your views here.
def post_manager(request):

    if request.method=='POST':
        obj=Manager()
        obj.name=request.POST.get('mn')
        obj.address= request.POST.get('adr')
        obj.qualification = request.POST.get('qlf')
        obj.password = request.POST.get('psw')
        obj.status='pending'
        obj.save()
        context={
            "msg":"Successfully Registered"
        }
        return render(request, 'manager/manager.html',context)
    return render(request, 'manager/manager.html')

def view_managemanager(request):
    obj=Manager.objects.all()
    context={
        'x':obj
    }
    return render(request,'manager/managemanager.html',context)

def approve(request,idd):
    obj=Manager.objects.get(manager_id=idd)
    obj.status='approved'
    obj.save()

    ob = Login()
    ob.user_name = obj.name
    ob.password = obj.password
    ob.type = 'manager'
    ob.u_id = obj.manager_id
    ob.save()
    message="Approved"
    mobj=Manager.objects.all()
    context={
        'msg':message,
        'x':mobj
    }
    return render(request,'manager/managemanager.html',context)

def reject(request,idd):
    obj=Manager.objects.get(manager_id=idd)
    obj.status='rejected'
    obj.save()
    message="Rejected"
    mobj=Manager.objects.all()
    context={
        'msg':message,
        'x':mobj
    }
    return render(request,'manager/managemanager.html',context)


def updt(request):
    # ss=
    obj=Manager.objects.all()
    context={
        'x':obj
    }
    if request.method=='POST':
        obj=Manager()
        obj.name=request.POST.get('mn')
        obj.address= request.POST.get('adr')
        obj.qualification = request.POST.get('qlf')
        obj.password = request.POST.get('psw')
        obj.status='pending'
        obj.turf_id =request.POST.get('mn')
        obj.save()
    return render(request, 'manager/update_profile.html', context)
