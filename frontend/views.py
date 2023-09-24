from django.views.generic import ListView, DetailView
from .models import Item


class ItemListView(ListView):
    model = Item
    template_name = "item_list.html"
    context_object_name = "items"
    paginate_by = 4


class ItemDetailView(DetailView):
    model = Item
    template_name = "item_detail.html"
