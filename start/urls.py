from django.urls import path
from .views import*

urlpatterns = [
    path('items',Create_Api.as_view(), name='create_item'),
    path('get_items', Get_data.as_view(), name='get_item'),
    path('update_items/<int:id>',Update_data.as_view(), name='update_item'),
    path('delete_items/<int:id>', Delete_data.as_view(), name='delete_item'),
]
