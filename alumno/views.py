from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.contrib.auth.models import User 

@login_required
def profile(request, id = -1):
    print(id)
    if request.method == 'GET':
        user = None
        if id == -1:
            user = get_object_or_404(User.objects, pk=request.user.id)
        else:
            user = get_object_or_404(User.objects, pk=id)
        print(user)
        return render(request, "site/profile.html", {'Usuario':user})