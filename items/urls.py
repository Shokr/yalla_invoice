from django.urls import path

from .views import *

app_name = 'items'

urlpatterns = [
    path('add', add_item, name='add_item'),
    path('edit/<int:pk>/', edit_item, name='edit_item'),
    path('delete/<int:pk>/', delete_item, name='delete_item'),
    path('<int:pk>/', view_item, name='view_item'),
    path('list', list_items, name='items'),
]
