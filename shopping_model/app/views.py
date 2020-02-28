from django.shortcuts import render
from . models import Products,OrderProducts,Order
from django.db.models import Q,CharField,TextField
from django.db.models.functions import Lower
from django.views.generic import View
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import pdb
from django.contrib import messages
# Create your views here.

def index(request):
    product_objects = Products.objects.all()
    CharField.register_lookup(Lower, "lower")
    TextField.register_lookup(Lower, "lower")
    item_name = request.GET.get('item_name')

    if item_name !='' and item_name is not None:
        item_name = item_name.strip().lower()
        product_objects = Products.objects.filter((Q(title__lower__icontains=item_name) | Q(category__lower__icontains=item_name) | Q(description__lower__icontains=item_name)))


    paginator = Paginator(product_objects, 8)

    try:
        page = int(request.GET.get('page',1))
    except:
        page = 1
    try:
        product_objects = paginator.page(page)
    except(EmptyPage, InvalidPage):
        product_objects = paginator.page(1)



     # Get the index of the current page
    index = product_objects.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    # Get our new page range. In the latest versions of Django page_range returns
    # an iterator. Thus pass it to list, to make our slice possible again.
    page_range = list(paginator.page_range)[start_index:end_index]
    return render(request,'app/index1.html',{'product_objects' : product_objects,'page_range':page_range})


def detail(request,id):
    product_object = Products.objects.get(id=id)

    return render(request,'app/detail1.html',{'product_object':product_object})

def checkout(request):
    # category_object = Products.objects.filter(category=cat)
    return render(request,'app/checkout.html')

class OrderSummaryView(View):
    # pdb.set_trace()
    def get(self,*args,**kwargs):
        order = Order.objects.get(user=self.request.user,ordered= False)
        # product_object = Products.objects.get(id=id)

        return render(self.request,'app/order_summary.html',{'order':order})





@login_required
def add_to_cart(request,id):
    # pdb.set_trace()
    product = get_object_or_404(Products,id=id)
    print(product)
    order_product,created = OrderProducts.objects.get_or_create(
    product=product,
    user = request.user,
    ordered = False)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    print(order_qs)
    if order_qs.exists():
        order = order_qs[0]
        #check if ordered product is in the order

        if order.items.filter(product__id=product.id).exists():
            print(order_product)
            order_product.quantity += 1
            order_product.save()
            messages.info(request,"this item quantity was updated")
            return redirect("OrderSummaryView")

        else:
            messages.info(request,"this item was added to your cart")
            order.items.add(order_product)

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,odered_date=ordered_date)
        order = order.items.add(order_product)

        messages.info(request,"this item was added to your cart")
    return redirect("index")

@login_required
def remove_cart(request,id):
    # pdb.set_trace()
    product = get_object_or_404(Products,id=id)
    print(product)

    order_qs = Order.objects.filter(user=request.user,ordered=False)
    print(order_qs)
    if order_qs.exists():
        order = order_qs[0]
        print(order)
        #check if ordered product is in the order
        if order.items.filter(product__id=product.id).exists():
            order_product = OrderProducts.objects.filter(
            product=product,
            user = request.user,
            ordered = False)[0]

            order.items.remove(order_product)
            messages.info(request,"this item was removed from your cart")
            return redirect("OrderSummaryView")
        else:
            # add a message that order dosen't contain the product
            order_product = OrderProducts.objects.filter(
            product=product,
            user = request.user,
            ordered = False)[0]
            print(order_product)
            order.items.remove(order_product)
            messages.info(request,"this item was not in your cart")

            return redirect("index")
    else:
        # add a message that user dosen't hsve a order
        messages.info(request,"you do not have an active order")
        return redirect("index")
    return redirect("index")

@login_required
def remove_single_item_from_cart(request,id):
    # pdb.set_trace()
    product = get_object_or_404(Products,id=id)
    print(product)

    order_qs = Order.objects.filter(user=request.user,ordered=False)
    print(order_qs)
    if order_qs.exists():
        order = order_qs[0]
        print(order)
        #check if ordered product is in the order
        if order.items.filter(product__id=product.id).exists():
            order_product = OrderProducts.objects.filter(
            product=product,
            user = request.user,
            ordered = False)[0]
            if order_product.quantity > 1:
                order_product.quantity -= 1
            else:
                order.items.remove(order_product)

            order_product.save()
            messages.info(request,"this item quantity was updated")
            return redirect("OrderSummaryView")

        else:
            # add a message that order dosen't contain the product
            order_product = OrderProducts.objects.filter(
            product=product,
            user = request.user,
            ordered = False)[0]
            print(order_product)
            # order.items.remove(order_product)
            messages.info(request,"this item was not in your cart")

            return redirect("index")
    else:
        # add a message that user dosen't hsve a order
        messages.info(request,"you do not have an active order")
        return redirect("index")
    return redirect("index")
