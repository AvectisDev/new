from django.urls import path
from filling_station import views


urlpatterns = [
    path('', views.index, name="home"),
    path('client/', views.client, name="client"),
    #path('client/loading/', views.loading, name='loading'),
    #path('client/unloading/', views.unloading, name='unloading'),
    path('operator/table/', views.operator, name='operator_table'),
    #path('driver/table/', views.driver, name='driver_table')
]