# paystack-py [![Build Status](https://travis-ci.com/iambenkay/paystack-py.svg?branch=master)](https://travis-ci.com/iambenkay/paystack-py)
For completing, initializing and verifying paystack transactions

New in 1.0.5:
    Now supports recurring debits and directly charging a card
    included tests

```python
from paystack_py import Paystack

ps = Paystack("<YOUR_API_KEY>")
```

#### For payments that redirect you to paystack.
```python
url = ps.init_redirect('test@test.com', 500000, 'https://callback.com/url')
```
#### Redirect to the URL returned and in your callback view get the ```reference``` GET parameter and pass it to verify:
```python
status = ps.verify(reference)

if status:
    # give value to customer
    pass
```
#### For recurring debits, instead of using verify above, use verify_and_authorize:
```python
    auth_code = ps.verify_and_authorize(reference)

    new_auth_code = ps.recurring_payments(auth_code, "test@test.com", 50000)

    # just keep storing each subsequent authorization code so you can use it later.
```
#### For charging cards:
```python
status = ps.charge_a_card(card={
        "number": "4084084084084081",
        "cvv": 408, 
        "expiry_month": 9,
        "expiry_year": y}, email="test@test.com", amount=500000)

if status:
    # Give customer value
    pass
```
