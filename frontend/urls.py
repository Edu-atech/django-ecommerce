from django.urls import path
from . import views

app_name = "frontend"

urlpatterns = [
    path("", views.ItemListView.as_view(), name="item-list"),
    path("item/<slug:slug>", views.ItemDetailView.as_view(), name="item-detail"),
]
