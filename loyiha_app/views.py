from django.shortcuts import render, get_object_or_404, redirect
from .models import Qurulmalar,Watch,Bacground
from .forms import QurulmalarForm, WatchForm



def qurulmalar_list(request):
    qurulmalar = Qurulmalar.objects.all()
    return render(request, 'qurulmalar_list.html', {'qurulmalar': qurulmalar})

def qurulmalar_detail(request, pk):
    qurulma = get_object_or_404(Qurulmalar, pk=pk)
    return render(request, 'qurulmalar_detail.html', {'qurulma': qurulma})

def qurulmalar_create(request):
    if request.method == 'POST':
        form = QurulmalarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('qurulmalar_list')
    else:
        form = QurulmalarForm()
    return render(request, 'qurulmalar_form.html', {'form': form})

def qurulmalar_update(request, pk):
    qurulma = get_object_or_404(Qurulmalar, pk=pk)
    if request.method == 'POST':
        form = QurulmalarForm(request.POST, request.FILES, instance=qurulma)
        if form.is_valid():
            form.save()
            return redirect('qurulmalar_list')
    else:
        form = QurulmalarForm(instance=qurulma)
    return render(request, 'qurulmalar_form.html', {'form': form})

def qurulmalar_delete(request, pk):
    qurulma = get_object_or_404(Qurulmalar, pk=pk)
    if request.method == 'POST':
        qurulma.delete()
        return redirect('qurulmalar_list')
    return render(request, 'qurulmalar_confirm_delete.html', {'qurulma': qurulma})



def index(request):
    qurilmalar = Qurulmalar.objects.all()
    watch = Watch.objects.all()
    bacground = Bacground.objects.all()

    return render(request, 'base.html', context={'qurilmalar':qurilmalar,'watchs':watch,'bacgrounds':bacground})
def checkout(request):
    return render(request, 'checkout.html')


