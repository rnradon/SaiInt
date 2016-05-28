from django.shortcuts import render
from django.http import HttpResponse
from .models import ItemCategory, ItemName
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
def index(request):

    all_item_cat = ItemCategory.objects.all()
    # template = loader.get_template('items/index.html')
    context = {
        'all_item_cat': all_item_cat,
    }
    # html = ''
    #
    # for items in all_Items:
    #     url = '/category/' + str(items.id)+'/'
    #     html += '<a href = "' + url + '">' + items.furniture_type + '</a><br>'
    # return HttpResponse(html)
    # return HttpResponse("<h1>A LIST OF ITEM CATEGORIES</h1>")

    # return HttpResponse(template.render(context,request))

    return render(request, 'items/index.html', context)

def items(request):
    return HttpResponse("<h2>ITEMS IN THAT CATEGORY</h2>")


def category(request, itemCat_name):
    # return HttpResponse("<h2>categorys for Item ID "+ str(itemCat_id)+" </h2>")
    # try:
    #     itemCat = ItemCategory.objects.get(pk = itemCat_id)
    # except ItemCategory.DoesNotExist:
    #     raise Http404("Album does not exists")
    itemCat = get_object_or_404(ItemCategory, furniture_type = itemCat_name)

    all_items = ItemName.objects.all().filter(itemcategory = itemCat)
    return render(request, 'items/category.html', {'all_items' : all_items})
def item(request, itemName):
    itemCat = get_object_or_404(ItemName, item_name = itemName)
    
