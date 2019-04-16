from django.test import TestCase
from .forms import OrderForm
from .forms import MakePaymentForm

# Create your tests here.
class TestCheckout(TestCase):
    
    def test_can_process_payment_with_only_name(self):
        form = OrderForm({'full_name': 'CreateTests'})
        self.assertFalse(form.is_valid())
        
    def test_no_submit_without_name(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        
    def test_no_submit_without_credit_card(self):
        form = MakePaymentForm({'Credit card number': ''})
        self.assertFalse(form.is_valid())