from django.conf.urls import include, url
from .import views
from .models import ItemCategory, ItemName

app_name = 'items'

urlpatterns = [
    # /category/
    url(r'^$',views.category ,name = 'category'),

    # /category/categoryName
    url(r'^(?P<item_name>Bed)/$', views.item, name = 'item'),
    url(r'^(?P<item_name>Sofa)/$', views.item, name = 'item'),
    url(r'^(?P<item_name>Chair)/$', views.item, name = 'item'),

]
