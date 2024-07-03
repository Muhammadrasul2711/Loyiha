from django.shortcuts import render
from .models import Qurulmalar,Watch,Bacground


def index(request):
    qurilmalar = Qurulmalar.objects.all()
    watch = Watch.objects.all()
    bacground = Bacground.objects.all()

    return render(request, 'base.html', context={'qurilmalar':qurilmalar,'watchs':watch,'bacgrounds':bacground})
def checkout(request):
    return render(request, 'checkout.html')


