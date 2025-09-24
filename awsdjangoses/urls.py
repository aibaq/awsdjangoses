from django.urls import path

from . import views

app_name = 'awsdjangoses'


urlpatterns = [
    path('bounces', views.AmazonSesViewSet.as_view({'post': 'bounces'}), name='aws-ses-bounces'),
    path('complaints', views.AmazonSesViewSet.as_view({'post': 'complaints'}), name='aws-ses-complaints'),
    path('delivery', views.AmazonSesViewSet.as_view({'post': 'delivery'}), name='aws-ses-delivery'),
]
