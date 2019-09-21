import requests


class Paystack:
    def __init__(self, api_key: str):
        """
        constructor for Paystack class
        :param api_key: API key to access paystack services
        """
        # store the api_key as a member of the class
        self.api_key = api_key

    def init_redirect(self, email, amount, callback_url):
        """
        initialize function to initiate a payment
        :param email: email of the paying user
        :param amount: amount to be paid
        :param callback_url: URL to reply to when payment is successful
        :return: bool
        """
        # we use try .. except to catch errors that might occur
        response_object = requests.post("https://api.paystack.co/transaction/initialize",
                                        data={
                                            "email": email,
                                            "amount": amount,
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

    def verify(self, reference):
        """
        A function to verify that a payment was received
        :param reference: the reference id of the transaction
        :return: bool
        """
        response = self._query_verify_route(reference)

        # if "status" is positive then the process worked
        return response.get("status")

    def verify_and_authorize(self, reference):
        """
        Used to get authorization code for recurring debits
        :param reference: the reference id of the transaction
        :return: str
        """
        # confirm that the payment has been completed
        if self.verify(reference):
            response = self._query_verify_route(reference)
            # return the auth code for recurring debits
            return response["data"]["authorization"]["authorization_code"]
        else:
            # return a falsy value if the payment has not been verified
            return None

    def _query_verify_route(self, reference):
        """
        Used to query the Paystack REST API verify/ endpoint
        :param reference: the reference id of the transaction
        :return: dict
        """
        # send a request to Paystack verification endpoint
        response_object = requests.get(f"https://api.paystack.co/transaction/verify/{reference}",
                                        headers={"Authorization": f"Bearer {self.api_key}"})

        # convert response object to a Dictionary and return it
        return response_object.json()

    def recurring_payments(self, authorization_code, email, account):
        """
        :param authorization_code: the user's authorization code to continually charge his card
        :param email: the user's email
        :param amount: the amount to send
        :return: bool
        """
        response_object = requests.get(f"https://api.paystack.co/charge_authorization",
                                        headers={"Authorization": f"Bearer {self.api_key}"},
                                        data={
                                            "authorization_code": authorization_code,
                                            "email": email,
                                            "amount": amount,
                                        })
        response = response_object.json()

        if response.get("status"):
            return response["data"]["authorization"]["authorization_code"]
        else:
            return None

    def charge_a_card(self, card, email, amount):
        """
        :param card: the user's card details
        :param email: the user's email
        :param amount: the amount to send
        :return: bool
        """

        # sends a POST request to the charge/ endpoint
        response_object = requests.post("https://api.paystack.co/charge",
                                        headers={"Authorization": f"Bearer {self.api_key}"},
                                        json={
                                            "card": card,
                                            "email": email,
                                            "amount": amount,
                                        })
        response = response_object.json()
        return response.get("status")

    def charge_a_bank(self, card, email, amount):
        # yet to be implemented
        raise NotImplementedError
