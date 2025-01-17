from datetime import datetime
from typing import List

from order_products.models import OrderProduct
from products.models import Product


class OrderProductServiceV1:

    @staticmethod
    def get_statistics(start_time: datetime, end_time: datetime) -> List[dict]:
        """
        Рассчитывает статистику использования продукта за указанный период.

        Args:
            start_time: Начало периода
            end_time: Конец периода

        Returns:
            List[dict] для каждого продукта с количеством часов в аренде и свободных часов и rent_total_amount
        """
        total_duration = (end_time - start_time).total_seconds() / 3600  # общая продолжительность в часах
        current_time = start_time
        products_statistics = []

        for product in Product.objects.all():
            rented_hours = 0
            order_products = OrderProduct.objects.filter(
                product=product,
                order__start_date__lt=end_time,
                order__end_date__gt=start_time,
            ).select_related('order').order_by('order__start_date')

            for order_product in order_products:
                # define start period rent
                period_start = max(current_time, order_product.order.start_date)
                # define end period rent
                period_end = min(end_time, order_product.order.end_date)

                if period_start < period_end:
                    # add total hours in rent
                    rental_hour = (period_end - period_start).total_seconds() / 3600
                    rented_hours += rental_hour

            free_hours = total_duration - rented_hours
            products_statistics.append({
                'product_name': product.name,
                'rent_total_amount': product.price * round(rented_hours),  # первое условие для статистики
                # второе условие для статистики
                'free_hours': round(free_hours),
                'rented_hours': round(rented_hours),
            })

        return products_statistics
