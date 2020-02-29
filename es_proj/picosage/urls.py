from django.urls import path

from . import views

app_name = 'picosage'
urlpatterns = [
    path('', views.index, name='index'),
    # All Properties
    path('properties/', views.properties_all, name='properties_all'),
    # Single Property
    path('properties/<int:property_id>/', views.property_single, name='property_details'),
]
