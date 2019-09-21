import pytest
import datetime
from . import index

ps = index.Paystack("sk_test_8e31ea60a3a6b4c890cd6dc090f4a9a96dc1031b")

def test_that_init_redirect_starts_with_paystack_link():
    assert ps.init_redirect("test@test.com", 500000, "http://www.callback123unk.com/urlopens12").startswith("https://checkout.paystack.com/")

def test_that_charging_a_valid_card_works():
    y = int(str(datetime.datetime.now().year)[2:]) + 1
    assert ps.charge_a_card(card={
        "number": "4084084084084081",
        "cvv": 408, 
        "expiry_month": 9,
        "expiry_year": y}, email="test@test.com", amount=500000)

def test_that_charging_an_invalid_card_works():
    y = int(str(datetime.datetime.now().year)[2:]) + 1
    assert not ps.charge_a_card({
        "number": "4084084084084082",
        "cvv": 408, 
        "expiry_month": 9,
        "expiry_year": y}, "test@test.com", 500000)
