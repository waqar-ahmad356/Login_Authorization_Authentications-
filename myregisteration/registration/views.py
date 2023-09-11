from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationForm
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from .models import Member
# Create your views here.
def home(request):
    template=loader.get_template('master.html')
    member=Member.objects.all().values()
    context={
        'member':member,
    }
    return HttpResponse(template.render(context,request))
class UserRegistrationView(View):
    def get(self,request):
       form=UserRegistrationForm()
       return render(request,'registration.html',locals())
    def post(self,request):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'SuccessFully Registered')
        else:
            messages.warning(request,'Invalid Data')
        return render(request,'registration.html',locals())
