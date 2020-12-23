from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'Question From ' + name,
            message,
            email,
            ['cmurray4492@gmail.com'],
        )
        return render(request, 'pages/contactus.html')
    else:
        return render(request, 'pages/contactus.html')


def usefulinfo(request):
    return render(request, 'pages/usefulinfo.html')
