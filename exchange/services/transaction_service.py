import random
import string
from datetime import datetime

from django.utils import timezone

from exchange.models import Transaction
from payments.models import Order
from services.util import CustomRequestUtil


def generate_trxn_ref(prefix="ECH"):
    """
    Generate a unique reference number for an order.

    Args:
        prefix (str): A prefix for the reference number (default is "ORD").

    Returns:
        str: A unique order reference number.
    """
    # Current timestamp in the format YYYYMMDDHHMMSS
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Random alphanumeric string of 6 characters
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # Combine prefix, timestamp, and random string
    ref_number = f"{prefix}-{timestamp}-{random_str}"

    return ref_number



class TransactionService(CustomRequestUtil):

    def create_single(self, payload):
        trxn = Transaction.available_objects.create(
            user=self.auth_user,
            coin=payload.get("coin"),
            wallet_address=payload.get("wallet_address"),
            bank_name=payload.get("bank_name"),
            account_name=payload.get("account_name"),
            account_number=payload.get("account_number"),
            trans_type=payload.get("trans_type"),
            rate=payload.get("rate"),
            amount_in_ngn=payload.get("amount_in_ngn"),
            amount_in_usd=payload.get("amount_in_usd"),
            amount_in_crypto=payload.get("amount_in_crypto"),
            ref=generate_trxn_ref()
        )
        return trxn

    def fetch_list(self):
        return self.get_base_query().filter(user=self.auth_user)

    def get_base_query(self):
        qs = Transaction.available_objects.select_related("user")

        return qs

    def fetch_single(self, ref):
        trxn = self.get_base_query().filter(ref=ref).first()
        if not trxn:
            return None, self.make_error("Transaction does not exist")

        return trxn, None