from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = "Crip"
    _context = {'date': date, 'name': name}
    return render(request, 'home.html', _context)


def test(request):
    return render(request, 'test.html')
