from django.shortcuts import render
from booking.models import Booking
from datetime import timedelta,datetime
from turf.models import Turf
from slot.models import Slot
from  payment.models import  Payment
from django.http import HttpResponseRedirect
from django.utils import timezone
from datetime import time
from payment.views import user_view_payment

# Create your views here.
def post_booking(request,idd):
    ss=request.session["u_id"]
    obb=Turf.objects.get(turf_id=idd)
    sob=Slot.objects.filter(turf_id=idd)
    context={
        'x':obb,
        's':sob
    }
    if request.method=='POST':
        d=request.POST.get('da')
        slote=request.POST.get('ti')
        sobj=Slot.objects.get(slot_id=slote)
        # Check date time  is greater than current date time
        current_datetime = timezone.now()
        date_to_check = datetime.strptime(d, "%Y-%m-%d").date()
        combined_datetime = datetime.combine(date_to_check, sobj.slot)
        if not timezone.is_aware(combined_datetime):
                    combined_datetime = timezone.make_aware(combined_datetime)
        if combined_datetime < current_datetime:
            message="Choose valid date and time"
            context={
                "msg":message,
                'x':obb,
                's':sob
            }
            return render(request, 'booking/booking.html',context)
        
        # Check slot is available
        bob=Booking.objects.filter(date=d,start_time=sobj.slot,turf_id=idd).exclude(status='rejected')
        if bob:
            message="The slot is already booked.Choose another one"
            context={
                "msg":message,
                'x':obb,
                's':sob
            }
            return render(request, 'booking/booking.html',context)
        else:
            obj=Booking()
            obj.date=d
            print(sobj.slot)
            obj.start_time=sobj.slot
            obj.end_time=sobj.e_time
            obj.status='Booked'
            obj.cancel_status='Booked'
            obj.turf_id=idd
            obj.user_id=ss
            obj.save()
            obj1=Payment()
            obj1.amount=obj.turf.price
            obj1.user_id=obj.user_id
            obj1.booking=obj
            obj1.status='pending'
            obj1.save() 
            message="Slot booked"
            context={
                "msg":message,
                'x':obb,
                's':sob
            }
            # return HttpResponseRedirect('/payment/post_payment/')
            # return render(request, 'payment/booking.html',context)
            return user_view_payment(request,obj1.pay_id)
    return render(request, 'booking/booking.html',context)


def user_viewbooking(request):
    uid=request.session["u_id"]
    obj=Payment.objects.filter(user_id=uid)
    context={
         'ob':obj
    }
    return render(request,'booking/user_viewbooking.html',context)


def view_managebooking(request):
    ss=request.session["u_id"]
    obj=Payment.objects.filter(booking__turf__manager__manager_id=ss,status='pending')
    print(obj)
    context={
        'x':obj
    }
    return render(request, 'booking/manage_booking.html',context)

def approve(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    obj.status='approved'
    obj.save()
    return view_managebooking(request)

def reject(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    obj.status='rejected'
    obj.save()
    return view_managebooking(request)



def view_booking(request):
    ss=request.session["u_id"]
    obj=Payment.objects.filter(booking__turf__manager__manager_id=ss)
    print(obj)
    context = {
        'x': obj
    }
    return render(request,'booking/viewbooking.html',context)


def cancel(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    obj.delete()
    return user_viewbooking(request)


# def view_cancelturf(request):
#     ss = request.session["u_id"]
#     obj = Booking.objects.filter(status='approved', user_id=ss)
#     context = {
#         'x': obj
#     }
#     return render(request,'booking/cancelturfbooking.html',context)


# def view_bookingstatus(request):
#     obj = Booking.objects.all()
#     context = {
#         'x': obj
#     }
#     return render(request,'booking/viewbookingststus.html',context)