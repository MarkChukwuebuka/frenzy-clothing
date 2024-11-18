from django.utils import timezone

from payments.models import Order
from services.util import CustomRequestUtil


class OrderService(CustomRequestUtil):

    def create_single(self, payload):
        order = Order.available_objects.create(
            user=self.auth_user,
            first_name=payload.get("first_name"),
            last_name=payload.get("last_name"),
            email=payload.get("email"),
            state=payload.get("state"),
            address=payload.get("address"),
            phone=payload.get("phone"),
            lga=payload.get("lga"),

        )

        return order

    def fetch_list(self):
        return self.get_base_query().filter(user=self.auth_user)

    def get_base_query(self):
        qs = Order.available_objects.select_related("user").prefetch_related("payment")

        return qs

    def fetch_single(self, order_id):
        order = self.get_base_query().filter(id=order_id).first()
        if not order:
            return None, self.make_error("Order does not exist")

        return order, None