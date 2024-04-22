from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import datetime 
from main.decorators import role_required


# @check_mode

@login_required
def app(request):
    return HttpResponseRedirect(reverse('index'))

# Create your views here.

@login_required
@role_required(['superadmin'])
def index(request):
    today = datetime.date.today() + datetime.timedelta(days=1)
    
    
    
    context = {
        'page_title' : 'Dashboard',
        
        
    }
    return render(request,'admin_panel/index.html', context)
