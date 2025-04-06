from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .form import ItemForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView



#function basic views
def index(request):
    item_list = Item.objects.all()
    context ={
         'item_list':item_list,
    }

    food_name =request.GET.get('food_name')
    if food_name != '' and food_name is not None:
      item_list = item_list.filter(name__icontains=food_name)

    return render(request,'food/index.html',context)

# class basic views
class IndexClassView(ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = 'item_list'


#function basic views
def item(request):
    return HttpResponse('item')


#function basic views
def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request,'food/detail.html',context)


# This is class basic views for deatail
class FoodDetail(DetailView):
     model = Item
     template_name = 'food/detail.html'



def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form':form})


#This is a class based view for create item
class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    success_url = reverse_lazy('food:index')
    template_name = 'food/item-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form) 
        
    
    


def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
     
    if form.is_valid():
        form.save() 
        return redirect('food:index')
    
    return render(request, 'food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
      item.delete()
      return redirect('food:index')

    return render(request, 'food/item-delete.html',{'item':item})



