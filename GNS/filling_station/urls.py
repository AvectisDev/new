from django.urls import path
from filling_station import views


urlpatterns = [
    # path('', views.index, name="home"),
    path('', views.reader1, name="ballons_table_1"),
    path('reader2/', views.reader2, name="ballons_table_2"),
    path('reader3/', views.reader3, name="ballons_table_3"),
    path('reader4/', views.reader4, name="ballons_table_4"),
    path('reader5/', views.reader5, name="ballons_table_5"),
    path('reader6/', views.reader6, name="ballons_table_6"),
    path('reader7/', views.reader7, name="ballons_table_7"),
    path('reader8/', views.reader8, name="ballons_table_8"),

    path('client/', views.client, name="client"),
    #path('client/loading/', views.loading, name='loading'),
    #path('client/unloading/', views.unloading, name='unloading')
]