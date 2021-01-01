from django.shortcuts import render


def hdocs(request):
    return render(request, 'hdocs/hdocs.html')
