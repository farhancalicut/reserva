from django.shortcuts import render

from login.models import Login
from user.models import User

# Create your views here.
def post_user(request):
    if request.method=='POST':
        obj=User()
        obj.password = request.POST.get('psw')
        # obj.age = request.POST.get('age')
        obj.name = request.POST.get('name')
        obj.contact_number = request.POST.get('phn')
        obj.save()

        ob = Login()
        ob.user_name = obj.name
        ob.password = obj.password
        ob.type = 'user'
        ob.u_id = obj.user_id
        ob.save()
        context={
            "msg":"Successfully Registered"
        }
        return render(request, 'user/user.html', context)
    return render(request, 'user/user.html')

def post_profile(request):
    message=''
    ss= request.session["u_id"]
    print(ss)
    obb=User.objects.get(user_id=ss)
    print(obb)
    context={
        'x':obb
    }
    if request.method=='POST':
        obj=User.objects.get(user_id=ss)
        # obj.password = request.POST.get('psw')
        # obj.age = request.POST.get('age')
        obj.name = request.POST.get('name')
        obj.contact_number = request.POST.get('phn')
        obj.save()
        message = "Profile Updated"
        context = {
            'msg': message
        }
    return render(request, 'user/profile.html', context)

def post_tutorial(request):
    ss= request.session["u_id"]
    obb=User.objects.get(user_id=ss)
    context={
        'x':obb
    }
    if request.method=='POST':
        obj=User.objects.get(user_id=ss)
        # obj.password = request.POST.get('psw')
        # obj.age = request.POST.get('age')
        # obj.name = request.POST.get('name')
        # obj.contact_number = request.POST.get('phn')
        # obj.save()
    return render(request, 'user/tutorial.html', context)

def post_tutorial2(request):
    ss= request.session["u_id"]
    obb=User.objects.get(user_id=ss)
    context={
        'x':obb
    }
    if request.method=='POST':
        obj=User.objects.get(user_id=ss)
        # obj.password = request.POST.get('psw')
        # obj.age = request.POST.get('age')
        # obj.name = request.POST.get('name')
        # obj.contact_number = request.POST.get('phn')
        # obj.save()
    return render(request, 'user/tutorial2.html', context)

def post_tutorial3(request):
    ss= request.session["u_id"]
    obb=User.objects.get(user_id=ss)
    context={
        'x':obb
    }
    if request.method=='POST':
        obj=User.objects.get(user_id=ss)
        # obj.password = request.POST.get('psw')
        # obj.age = request.POST.get('age')
        # obj.name = request.POST.get('name')
        # obj.contact_number = request.POST.get('phn')
        # obj.save()
    return render(request, 'user/tutorial3.html', context)

def post_tutorial4(request):
    ss= request.session["u_id"]
    obb=User.objects.get(user_id=ss)
    context={
        'x':obb
    }
    if request.method=='POST':
        obj=User.objects.get(user_id=ss)
        # obj.password = request.POST.get('psw')
        # obj.age = request.POST.get('age')
        # obj.name = request.POST.get('name')
        # obj.contact_number = request.POST.get('phn')
        # obj.save()
    return render(request, 'user/tutorial4.html', context)

def view_user(request):
    obj=User.objects.all()
    context={
        'x':obj
    }
    return render(request,'user/view_user.html', context)

