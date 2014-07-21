from django.shortcuts import render

# Log this user into all of ASG's services
def sso_login(request):
    return render(request, 'login.html', locals())
