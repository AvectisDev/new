from django.urls import path
from filling_station import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('', views.index, name="home"),
    path('reader/<str:reader>', views.reader_info, name="ballons_table"),
    path('api/GetBalloonPassport', views.apiGetBalloonPassport, name="ballons_table"),
    path('api/UpdateBalloonPassport', views.apiUpdateBalloonPassport, name="ballons_table"),
    path('client/', views.client, name="client"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('client/loading/', views.loading, name='loading'),
    #path('client/unloading/', views.unloading, name='unloading')
]
