from django.shortcuts import render
from assignmanager.models import AssignManager
from manager.models import Manager
from turf.models import Turf
import datetime

# Create your views here.

def post_assignmanager(request):
    obb=Manager.objects.all()
    obb1=Turf.objects.all()
    context={
        'x':obb,
        'y':obb1
    }
    if request.method=='POST':
        obj=AssignManager()
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.manager_id=request.POST.get('mn')
        obj.turf_id=request.POST.get('tid')
        obj.save()
    return render(request, 'assignmanger/assignmanager.html',context)


def view_assign(request):
    obj=AssignManager.objects.all()
    context={
        'x':obj
    }
    return render(request,'assignmanger/view_assign.html', context)