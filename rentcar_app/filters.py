import django_filters
from rentcar_app.models import Car


class CarFilter(django_filters.FilterSet):  # Simple django filter definition that allows to filter car model by brand, type, fuel and gears
    class Meta:
        model = Car
        fields = ('brand', 'type', 'fuel', 'gears')



