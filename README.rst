# paystack-py
For completing, initializing and verifying paystack transactions

simply import the `Paystack` class from the package and use it to initialize and verify transactions.

    from paystack_py import Paystack

    ps = Paystack("<YOUR_API_KEY>")

    # To initiate a new Direct Payment

    url = ps.initialize('test@test.com', 50000, 'https://callback.com/url')

    # just redirect to the URL returned and in your callback view do

    reference = request.GET.get("reference") ) # reference is a GET parameter from the request

    status = ps.verify(reference)

    if status:
        # give value to customer
        pass