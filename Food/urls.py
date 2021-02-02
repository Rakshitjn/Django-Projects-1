
from django.urls import path,include
from . import views

app_name = 'food'
urlpatterns = [
    #/food/
    path('',views.index,name = 'home'),
    #/food1/
    path('<int:item_id>/',views.detail,name = 'details'),
    #add new item
    path('add',views.create_item,name = 'create_item'),
    #edit
    path('update/<int:id>',views.edit_item,name = 'edit_item'),
    #delete
    path('delete/<int:id>/',views.delete_item,name = 'delete_item')
]