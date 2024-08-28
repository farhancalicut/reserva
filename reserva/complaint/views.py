from django.shortcuts import render
from complaint.models import Complaint
import datetime
from django.http import HttpResponseRedirect
# Create your views here.
def post_complaints(request):
    message=""
    ss=request.session["u_id"]
    if request.method=='POST':
        obj=Complaint()
        obj.complaint=request.POST.get('comp')
        obj.date_time=datetime.datetime.now()
        obj.status='pending'
        obj.user_id=ss
        obj.save()
        message = "Submitted successfully"
    context = {
            'msg': message
        }
        # return HttpResponseRedirect('/temp/user/')
    return render(request, 'complaint/complains.html', context)

def post_replay(request,idd):
    if request.method=="POST":
        obj=Complaint.objects.get(comp_id=idd)
        obj.replay=request.POST.get('rep')
        obj.status='replied'
        obj.save()
        return view_complaint(request)
    return render(request, 'complaint/replay.html')


def view_complaint(request):
    obj = Complaint.objects.all()
    context = {
        'x': obj
    }
    return render(request,'complaint/viewcomplient.html',context)


def view_replay(request):
    ss=request.session["u_id"]
    obj = Complaint.objects.filter(user_id=ss)
    context = {
        'x': obj
    }
    return render(request,'complaint/viewreplay.html',context)


def user_view_complaint(request):    
    ss=request.session["u_id"]
    obj = Complaint.objects.filter(user_id=ss,status='pending')
    context = {
        'x': obj
    }
    return render(request,'complaint/user_view_complaint.html',context)

def delete_complaint(request,idd):
    ob=Complaint.objects.get(comp_id=idd)
    ob.delete()
    return HttpResponseRedirect('/complaint/userv_compl/')


def user_view_reply(request):    
    ss=request.session["u_id"]
    obj = Complaint.objects.filter(user_id=ss,status='replied')
    context = {
        'x': obj
    }
    return render(request,'complaint/user_view_reply.html',context)