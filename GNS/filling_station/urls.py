from django.urls import path
from filling_station import views as filling_station_views


urlpatterns = [
    path('', filling_station_views.index, name="home"),
    #path('client/', filling_station_views.client, name="client"),
    #path('client/loading/', filling_station_views.loading, name='loading'),
    #path('client/unloading/', filling_station_views.unloading, name='unloading'),
    #path('operator/table/', filling_station_views.operator, name='operator_table'),
    #path('driver/table/', filling_station_views.driver, name='driver_table')
]