from django.shortcuts import render
from . models import Products
from django.db.models import Q,CharField,TextField
from django.db.models.functions import Lower
from django.core.paginator import Paginator
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

    return render(request,'app/detail.html',{'product_object':product_object})
