from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def vorota_otkatka(request):
    return render(request, 'main/vorota_otkatka.html')


def vorota_raspashka(request):
    return render(request, 'main/vorota_raspashka.html')


def vorota_garage(request):
    return render(request, 'main/vorota_garage.html')


def kalitka(request):
    return render(request, 'main/kalitka.html')


def servis(request):
    return render(request, 'main/services.html')


def contacts(request):
    return render(request, 'main/contacts.html')
