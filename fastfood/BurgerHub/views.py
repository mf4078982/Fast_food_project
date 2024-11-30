from django.shortcuts import render,get_object_or_404,redirect

from .models import MenuItem
from .forms import MenuItemForm

def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu_list.html', {'items': items})


def add_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm()
    return render(request, 'add_item.html', {'form': form})













def edit_item(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form, 'item': item})

def delete_item(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('menu_list')
    return render(request, 'delete_item.html', {'item': item})
