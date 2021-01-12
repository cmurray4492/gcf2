from django.shortcuts import render


def hdocs(request):
    return render(request, 'hdocs/hdocs.html')


def declaration_of_independence(request):
    return render(request, 'hdocs/declaration_of_independence.html')


def us_constitution(request):
    return render(request, 'hdocs/us_constitution.html')


def us_bill_of_right(request):
    return render(request, 'hdocs/us_bill_of_rights')
