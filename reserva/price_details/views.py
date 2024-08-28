from django.shortcuts import render
from price_details.models import PriceDetails
from turf.models import Turf
# Create your views here.
def post_price(request):
    obb=Turf.objects.all()
    context={
        'x':obb
    }
    if request.method=='POST':
        obj=PriceDetails()
        obj.turf_id=request.POST.get('mn')
        obj.price=request.POST.get('price')
        obj.save()
    return render(request, 'price_details/price.html',context)

def view_pricedetails(request):
    obj=PriceDetails.objects.all()
    context={
        'x':obj
    }
    return render(request,'price_details/viewpricedetails.html',context)

def view_rate(request):
    obj = PriceDetails.objects.all()
    context = {
        'x': obj
    }
    return render(request,'price_details/viewrate.html',context)