from django.shortcuts import render
from django.views import generic
from .models import Item,Order,Category,ItemQuantity
import json
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect

def redirection(request):
    o=redirect(f"/smart_restaurant/1")
    return o

def index(request,table_no):
    return render(request,'smart_restaurant/index.html',{'table_no':table_no})

def menu(request):
    try:
        table_no=request.POST['table_no']
    except:
        table_no=0
    categories=Category.objects.all()
    return render(request,'smart_restaurant/menu.html',{'categories':categories,'table_no':table_no})

def order_details(request):
    item_ids=[item.id for item in Item.objects.all()]
    item_quantity=[]
    try:
        for id in item_ids:
            quantity=request.POST[str(id)]
            if(quantity):
                item={'item':Item.objects.get(id=id),'quantity':quantity}
                item_quantity.append(item)
    except:
        item_quantity=[]
    try:
        table_no=request.POST['table_no']
    except:
        table_no=0
    return render(request,'smart_restaurant/order.html',{'item_quantity':item_quantity,'table_no':table_no})

def thanks(request):
    item_ids=[item.id for item in Item.objects.all()]
    item_quantity=[]
    try:
        for id in item_ids:
            try:
                quantity=request.POST[str(id)][0]
            except:
                quantity=0
            if(quantity):
                item={'item':Item.objects.get(id=id),'quantity':quantity}
                item_quantity.append(item)
                print(item)
    except:
        item_quantity=[]
    try:
        table_no=request.POST['table_no']
    except:
        table_no=0
    print(request.POST)
    new_order=Order(table_no=table_no)
    new_order.save()
    for item in item_quantity:
        item_q_object=ItemQuantity(order=new_order,item=item['item'],quantity=int(item['quantity']))
        item_q_object.save()
    new_order.save()
    ref_id=new_order.id
    return render(request,'smart_restaurant/thanks.html',{'ref_id':ref_id,'table_no':table_no})
    

    


