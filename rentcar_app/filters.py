import django_filters
from rentcar_app.models import Car


class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = ('brand', 'type')



