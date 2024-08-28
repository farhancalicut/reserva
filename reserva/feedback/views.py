from django.shortcuts import render
from feedback.models import Feedback
# Create your views here.
def post_feedback(request):
    message=""
    ss= request.session["u_id"]
    if request.method=='POST':
        obj=Feedback()
        obj.feedback=request.POST.get('feed')
        obj.user_id=ss
        obj.save()
        message = "Submitted successfully"
    context = {
        'msg': message
    }
    return render(request, 'feedback/feedback.html', context)

def veiw_feeds_manager(request):
    obj = Feedback.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'feedback/view_feed_manager.html',context)

def view_feed(request):
    obj=Feedback.objects.all()
    context={
        'a':obj
    }
    return render(request, 'feedback/viewfeedback.html', context)

def view_feed_afmin(request):
    obb = Feedback.objects.all()
    context = {
        'a':obb
    }
    return render(request,'feedback/viewfeedback.html',context)