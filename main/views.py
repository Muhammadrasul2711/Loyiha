from django.shortcuts import render, get_object_or_404, redirect
from loyiha_app.models import Watch
from loyiha_app.forms import  WatchForm


def watch_list(request):
    watches = Watch.objects.all()
    return render(request, 'admin/watch_list.html', {'watches': watches})

def watch_detail(request, id):
    watch = get_object_or_404(Watch, id=id)
    return render(request, 'admin/watch_detail.html', {'watch': watch})

def watch_create(request):
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('watch_list')
    else:
        form = WatchForm()
    return render(request, 'admin/watch_form.html', {'form': form})

def watch_update(request, id):
    watch = get_object_or_404(Watch, id=id)
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES, instance=watch)
        if form.is_valid():
            form.save()
            return redirect('watch_list')
    else:
        form = WatchForm(instance=watch)
    return render(request, 'admin/watch_form.html', {'form': form})

def watch_delete(request, id):
    watch = get_object_or_404(Watch, id=id)
    if request.method == 'POST':
        watch.delete()
        return redirect('watch_list')
    return render(request, 'admin/watch_confirm_delete.html', {'watch': watch})

