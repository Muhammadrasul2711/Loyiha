from django.shortcuts import render,get_object_or_404,redirect
from loyiha_app.models import Qurulmalar
from loyiha_app.forms import QurulmalarForm






def qurulmalar_list(request):
    qurulmalar =Qurulmalar.objects.all()
    return render(request,'admin/qurulmalar_list.html',{'qurulmalars':qurulmalar})




def qurulmallar_detail(request, id):
    qurulmalar=get_object_or_404(Qurulmalar,id)
    return render(request,'admin/qurulamar_detail.html',{'qurulmalar':qurulmalar})



def qurulmlar_create(request):
    if request.method == 'POST':
        form=QurulmalarForm(request.POST,request.FILES)
        if form.is_valid():
            qurulmalar=form
            qurulmalar.save()
            return redirect('qurulmalar_list')
    else:
        form=QurulmalarForm()
    return render(request, 'admin/qurulmalar_form.html', {'form': form})



def qurulmalar_update(request, id):
    qurulma = get_object_or_404(Qurulmalar, id=id)
    if request.method == 'POST':
        form = QurulmalarForm(request.POST, request.FILES, instance=qurulma)
        if form.is_valid():
            form.save()
            return redirect('qurulmalar_list')
    else:
        form = QurulmalarForm(instance=qurulma)
    return render(request, 'admin/qurulmalar_form.html', {'form': form})



def qurulmalar_delete(request, id):
    qurulma = get_object_or_404(Qurulmalar, id=id)
    if request.method == 'POST':
        qurulma.delete()
        return redirect('qurulmalar_list')
    return render(request, 'admin/qurulmalar_confirm_delete.html', {'qurulma': qurulma})








