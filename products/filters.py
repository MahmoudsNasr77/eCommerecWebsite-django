import django_filters
from .models import product
class ProductFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(lookup_expr='icontains' ,)
    class Meta:
        model = product
        fields = ('name',)
        



