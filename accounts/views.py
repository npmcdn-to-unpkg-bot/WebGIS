from django.core.mail import send_mail
from django.shortcuts import redirect
#from django.http import HttpResponsePermanentRedirect

def send_login_email(request):
#    return HttpResponsePermenantRedirect('/')
    return redirect('/')


'''
def send_login_email(request):
    email = request.POST['email']
    print(type(send_mail))
    send_mail(
        'Your login link for the Portal',
        'body text here',
        'noreply@webgisportal',
        [email],
    )
    return redirect('/')
'''
