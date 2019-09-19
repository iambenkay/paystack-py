import requests


class Paystack:
    def __init__(self, api_key: str):
        """
        constructor for Paystack class
        :param api_key: API key to access paystack services
        """
        # store the api_key as a member of the class
        self.api_key = api_key

    def initialize(self, email, amount, callback_url):
        """
        initialize function to initiate a payment
        :param email: email of the paying user
        :param amount: amount to be paid
        :param callback_url: URL to reply to when payment is successful
        :return: bool
        """
        # Paystack reads whatever amount we send as kobo
        amount_in_kobo = amount * 100
        # we use try .. except to catch errors that might occur
        try:
            response_object = requests.post("https://api.paystack.co/transaction/initialize",
                                            data={
                                                "email": email,
                                                "amount": amount_in_kobo,
                                                "callback_url": callback_url,
                                            },
                                            headers={"Authorization": f"Bearer {self.api_key}"})

            # convert response object to a Dictionary
            response = response_object.json()

            # make sure it has the "status property"
            if response.get("status"):
                return response.get("data").get("authorization_url")
            else:
                return False
        except requests.ConnectionError:
            print("There was a connection error")
            return False
        except KeyError:
            print("You have a problem with your API key")
            return False

    def verify(self, reference):
        """
        A function to verify that a payment was received
        :param reference: the reference id of the transaction
        :return: bool
        """
        try:
            # send a request to Paystack verification endpoint
            response_object = requests.get(f"https://api.paystack.co/transaction/verify/{reference}",
                                           headers={"Authorization": f"Bearer {self.api_key}"})

            # convert response object to a Dictionary
            response = response_object.json()

            # if "status" is positive then the process worked
            return True if response.get("status") else False

        except requests.ConnectionError:
            print("There was a connection error")
            return False
