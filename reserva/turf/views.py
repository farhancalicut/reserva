from django.shortcuts import render
from turf.models import Turf
from django.core.files.storage import FileSystemStorage

# Create your views here
def post_turf(request):
    message=""
    ss=request.session["u_id"]
    if request.method=='POST':
        obj=Turf()
        obj.password=request.POST.get('psw')
        obj.place=request.POST.get('adr')
        obj.turf_name=request.POST.get('tn')
        obj.categoty=request.POST.get('ctg')
        obj.price=request.POST.get('pp')
        obj.longitude=request.POST.get('long')
        obj.latitude=request.POST.get('lati')
        # obj.image=request.POST.get('img')
        myfile=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.image=myfile.name
        obj.status='Aproved'
        obj.manager_id=ss
        obj.save()
        message="Registered"
    context={
            'msg':message
    }

        # return render(request, 'turf/turf.html', context)
    return render(request, 'turf/turf.html',context)

def view_turf(request):
    if request.method=="POST":
        vv=request.POST.get('search')
        obj=Turf.objects.filter(address__icontains=vv)
        context={
            'x':obj
        }
    else:
        obj = Turf.objects.all()
        context = {
            'x': obj
        }
    return render(request,'turf/viewturf.html',context)
def view_manageturf(request):
    obj=Turf.objects.all()
    context={
        'x':obj
    }
    return render(request, 'turf/view_manageturf.html', context)

def approve(request,idd):
    obj=Turf.objects.get(turf_id=idd)
    obj.status='approved'
    obj.save()
    message="Approved"
    mobj=Turf.objects.all()
    context={
        'msg':message,
        'x':mobj
    }
    return render(request, 'turf/view_manageturf.html', context)

def reject(request,idd):
    obj=Turf.objects.get(turf_id=idd)
    obj.status='rejected'
    obj.save()
    message="Rejected"
    mobj=Turf.objects.all()
    context={
        'msg':message,
        'x':mobj
    }
    return render(request, 'turf/view_manageturf.html', context)



def manager_viewturf(request):
    uid=request.session["u_id"]
    obj=Turf.objects.filter(manager__manager_id=uid)
    context={
        'x':obj
    }

    return render(request,'turf/manager_viewturf.html',context)



def map(request,idd):
    obj=Turf.objects.get(turf_id=idd)
    context={
        'lat': obj.latitude,
        'lon': obj.longitude,
    }
    return render(request, 'turf/map.html', context)