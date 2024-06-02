from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

"""def dashboard_view(request):
    if not request.user.is_authenticated:
        return HttpResponse("Get login ol")
    return render(request, 'dashboard/dashboard.html')"""

@login_required(login_url='login_views')
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')