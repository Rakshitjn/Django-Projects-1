
from django.urls import path,include
from . import views

app_name = 'food'
urlpatterns = [
    #/food/
    path('',views.index,name = 'home'),
    #/food1/
    path('<int:item_id>/',views.detail,name = 'details'),
]