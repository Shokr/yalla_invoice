from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from items.forms import *


# Create your views here.

@login_required
def add_item(request):
    if request.method == 'POST':
        created_item_pk = None
        filled_form = ItemForm(request.POST)
        if filled_form.is_valid():
            created_item = filled_form.save()
            created_item_pk = created_item.pk
            filled_form = ItemForm()
        else:
            new_form = ItemForm()

        return redirect('items:items')
    else:
        form = ItemForm()
        return render(request, 'item/add_item.html', {'ItemForm': form})


@login_required
def edit_item(request, pk):
    item = Item.objects.get(pk=pk)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        filled_form = ItemForm(request.POST, instance=item)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            return render(request, 'item/edit_item.html', {'ItemForm': form, 'item': item})
        # return redirect('items:items')
    return render(request, 'item/edit_item.html', {'ItemForm': form, 'item': item})


@login_required
def view_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item/view_item.html', {'item': item})


@login_required
def list_items(request):
    items = Item.objects.get_queryset()
    return render(request, 'item/items.html', {'items': items})


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('items:items')
