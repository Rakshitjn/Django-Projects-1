from django.shortcuts import render,HttpResponse,redirect
from .models import Item
from django.template import loader
from .forms import ItemForm
# Create your views here.
def index(request):
    item_list = Item.objects.all()
    
    context = {
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)

def detail(request,item_id):
    item = Item.objects.get(pk = item_id)
    context = {
        'item':item,
    }
    return render(request,'food/details.html',context)
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:home')
    return render(request,'food/item_form.html',{'form':form})

def edit_item(request,id):
    item = Item.objects.get(id = id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item_form.html',{'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(id = id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:home')

    return render(request,'food/delete_item.html',{'item':item})