from .models import Product
from .tables import ProductTable

from django_tables2 import SingleTableView


# Create your views here.

class ShowProducts(SingleTableView):
    model = Product
    table_class = ProductTable
    template_name = 'products/overview.html'
