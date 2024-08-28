from django.shortcuts import render
from turf.models import Turf
from slot.models import Slot
from django.db.models import Q
from datetime import timedelta,datetime
# Create your views here.

def add_slot(request):
    uid=request.session["u_id"]
    tob=Turf.objects.filter(manager__manager_id=uid)
    context={
        'ob':tob
    }

    if request.method=='POST':        
        turf=request.POST.get('turf')
        
        start_time_str = request.POST.get('start_time')
        start_time = datetime.strptime(start_time_str, '%H:%M').time()

        # Calculate end_time by adding one hour to start_time
        time_difference = timedelta(hours=1)
        end_datetime = datetime.combine(datetime.today(), start_time) + time_difference
        etime=end_datetime.time()

        # check the time slot is alredy added
        obj=Slot.objects.filter(Q(turf__turf_id=turf) & ( Q(slot__lte=start_time,e_time__gt=start_time) | Q(slot__lt=etime,e_time__gt=etime)) )
        if obj:
            message="Slot already exist"
            context={
                'msg':message,
                'ob':tob
            }
            return render(request,'slot/add_slot.html',context)
        
        else:
            ob=Slot()
            ob.turf_id= turf 
            ob.slot = start_time    
            ob.e_time = etime
            ob.save()  
            message="Slot added"
            context={
                'msg':message,
                'ob':tob
            }
       
    return render(request,'slot/add_slot.html',context)


def view_slot(request,idd):
    obj=Slot.objects.filter(turf_id=idd)
    context={
        's':obj
    }
    return render(request,'slot/view_slot.html',context)


def delete_slot(request,idd):
    ob=Slot.objects.get(slot_id=idd)
    tid=ob.turf_id
    ob.delete()
    obj=Slot.objects.filter(turf_id=tid)
    print(obj)
    context={
        'msg':"deleted",
        's':obj
    }
    return render(request,'slot/view_slot.html',context)