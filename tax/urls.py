from django.urls import path
from . import views


urlpatterns = [
    path("", views.Default,name="Default"),
    path("<int:tax>/", views.caltax,name="caltax"),
    path("taxrate/", views.tax,name="tax")
    #path("<str:name>", views.tax,name="tax")
]