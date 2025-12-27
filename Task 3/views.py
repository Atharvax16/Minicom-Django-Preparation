from django.shortcuts import render,redirect,get_object_or_404
from .models import Items


def item_list(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        if name:
            Items.objects.create(name = name)
        return redirect("item_list")
    
    items = Items.objects.all()
    return render(request,"items/item_list.html",{
        'items':items
    })


def delete(request,item_id):
    if request.method == 'POST':
        item = get_object_or_404(Items,id = item_id)
        typed_name = request.POST.get("name")
        if typed_name and typed_name.strip() == item.name:
            item.delete()

    return redirect("item_list")

    