from django.shortcuts import render, redirect

# Log this user into all of ASG's services
def sso_login(request):
    if 'sso_redirect' not in request.GET:
        return redirect('https://asg.northwestern.edu')

    return render(request, 'login.html', locals())
