from django.conf.urls import include, url
from .import views
from .models import ItemCategory, ItemName

app_name = 'items'
# all_item_cat = ItemCategory.objects.all()
# all_item_cat
# extra_patterns = [
#     url(r'^all_item_cat/$', views.category),
# ]
urlpatterns = [
    # /category/
    url(r'^$',views.index ,name = 'index'),

    # /category/categoryName
    url(r'^(?P<itemCat_name>Wooden)/$', views.category, name = 'category'),
    url(r'^(?P<itemCat_name>Plastic)/$', views.category, name = 'category'),
    url(r'^(?P<itemCat_name>Steel)/$', views.category, name = 'category'),

    #category/categoryName/ItemName
    # url(r'^(?P<itemCat_name>)/', include(extra_patterns), name = 'category'),

]
