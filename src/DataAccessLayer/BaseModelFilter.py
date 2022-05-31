from django_filters import FilterSet, OrderingFilter


class BaseModelFilter(FilterSet):
    order_by = OrderingFilter(
        fields=(
            ('created_at', 'created_at')
        )
    )