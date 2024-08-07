from django.urls import path
from qurulmalarapp.views import (qurulmalar_list,qurulmalar_delete,
qurulmlar_create,qurulmallar_detail,qurulmalar_update)


urlpatterns = [
    path('qurulmalar/', qurulmalar_list, name='qurulmalar_list'),
    path('qurulmalar/<int:pk>/', qurulmallar_detail, name='qurulmalar_detail'),
    path('qurulmalar/create/', qurulmlar_create, name='qurulmalar_create'),
    path('qurulmalar/<int:pk>/edit/', qurulmalar_update, name='qurulmalar_update'),
    path('qurulmalar/<int:pk>/delete/', qurulmalar_delete, name='qurulmalar_delete'),

 ]
