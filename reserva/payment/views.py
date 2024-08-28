from django.shortcuts import render
from payment.models import Payment
from datetime import datetime,date
from booking.models import Booking
from django.http import HttpResponseRedirect
# Create your views here.
def post_payment(request,idd):
    message=""
    obb=Payment.objects.get(pay_id=idd)
    context={
        'x':obb
    }
    if request.method=='POST':
        obj=Payment.objects.filter(pay_id=idd,status='paid')
        if obj:
            message="Alredy paid"
            context={
                'msg':message,
                'x':obb
            }
            return (request,'payment/payment.html',context)
        else:
            obb.date=date.today()
            obb.time=datetime.now()
            obb.status='paid'
            obb.save()
            message = "Slot booked Successfully"
            context = {
                'msg':message
            }
            # return user_paymenthistory(request)
    return render(request,'payment/payment.html',context)

def view_payment(request):
    ss= request.session["u_id"]
    ob=Payment.objects.filter(booking__turf__manager_id=ss, status='paid')
    context={
        'x':ob
    }
    return render(request, 'payment/viewpayment.html', context)


def user_view_payment(request,idd):
    ss=request.session["u_id"]
    # ob=Payment.objects.filter(user_id=ss,status='pending',booking__status='approved')
    ob=Payment.objects.get(pay_id=idd)
    context={
        'i':ob
    }
    return render(request, 'payment/userviewpayment.html', context)


def user_paymenthistory(request):
    ss=request.session["u_id"]
    ob=Payment.objects.filter(user_id=ss,status='paid')
    context={
        'p':ob
    }
    return render(request, 'payment/userpayment_history.html', context)