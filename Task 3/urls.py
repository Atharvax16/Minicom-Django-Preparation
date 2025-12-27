from django.urls import path
from .views import item_list,delete

urlpatterns = [
    path("",item_list,name = "item_list"),
    path("delete/<int:item_id>/",delete,name = 'delete')
]  #name = 'item_list' is necessary because it is required for redirect('item_list')

