from django.urls import path, re_path
from order import views

app_name = 'order'
urlpatterns = [
    # /order/
    path("", views.OrderLV.as_view(), name="index"),
]