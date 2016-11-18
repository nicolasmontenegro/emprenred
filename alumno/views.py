from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.contrib.auth.models import User 

@login_required
def profile(request, id = -1):
    print(id)
    if request.method == 'GET':
        user = None
        if id == -1:
            user = User.objects.get(pk=request.user.id)
        else:
            user = User.objects.get(pk=id)
        print(user)
        return render(request, "site/profile.html", {'Usuario':user})