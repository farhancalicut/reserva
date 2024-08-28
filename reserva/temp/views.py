from django.shortcuts import render
from turf.models import Turf
from feedback.models import Feedback
# Create your views here.

def admin(request):
    return render(request, 'temp/admin.html')

def home(request):
    return render(request, 'temp/home.html')

def manager(request):
    return render(request, 'temp/manager.html')

def user(request):
    obj = Turf.objects.all()
    # obj1=Feedback.objects.all()
    context = {
        'x': obj,
        # 'y':obj1
    }
    return render(request, 'temp/user.html',context)

def user_2_home(request):
    return render(request,'temp/user_2_home.html')

def manager_2_home(request):
    return render(request,'temp/manager_2_home.html')

def admin_2_home(request):
    return render(request,'temp/admin_2_home.html')

def home_base(request):
    return render(request, 'temp/home_base.html')

def view_turf(request):
    obj=Feedback.objects.all()
    context={
        'y':obj
    }
    return render(request, 'temp/user.html',context)