from django.shortcuts import render


def hdocs(request):
    return render(request, 'hdocs/hdocs.html')


def declaration_of_independence(request):
    return render(request, 'hdocs/declaration_of_independence.html')
