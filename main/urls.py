from django.urls import path
from main.views import (
    watch_list, watch_detail, watch_create, watch_update, watch_delete
)

urlpatterns = [

    path('watches/', watch_list, name='watch_list'),
    path('watches/<int:id>/', watch_detail, name='watch_detail'),
    path('watches/create/', watch_create, name='watch_create'),
    path('watches/<int:id>/edit/', watch_update, name='watch_update'),
    path('watches/<int:id>/delete/', watch_delete, name='watch_delete'),
]

