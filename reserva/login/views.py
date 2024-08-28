from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login
# Create your views here.
def post_login(request):
    if request.method =="POST":
        name=request.POST.get("un")
        password=request.POST.get("psw")
        obj=Login.objects.filter(user_name=name,password=password)
        tp = ""
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp=="admin":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp=="manager":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/manager/')
            elif tp=="user":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/user/')
        else:
            objilist="Incorrect Username or Password...please check it!"
            context={
                "msg": objilist,
            }
            return render(request,'login/login.html', context)
    return render(request, 'login/login.html')
