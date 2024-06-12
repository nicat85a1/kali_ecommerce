import stripe


class Stripe:
    __success_url = "https://example.com/success"
    __api_key = "sk_test_51POMm7JfAZnXoOVRhmmlydJsS5lwQiqxEJMwXg898cBoExsfJI4x5zBTRS5JUlylstHxc7lNOFyrR5cMDW9U3KMt00pC0tMXOl"

    def __init__(self):
        self.__payment_url = None
        self.__transaction_id = None
        self.__payment_intent_id =None
        self.autenticate()

    def autenticate(self):
        stripe.api_key = self.__api_key

    def transaction(self, amount):
        response = stripe.checkout.Session.create(
            success_url= self.__success_url,
            line_items=[{"price_data": {
                                    "unit_amount": int(float(amount)*100), 
                                    "currency": "USD", 
                                    "product_data": {
                                        "name": "Donation"
                                    }},
                        "quantity": 1
                        }],
            mode="payment",
        )

        self.__payment_url = response['url']
        self.__transaction_id = response["id"]

    def retrive_func(self, transaction_id):
        response = stripe.checkout.Session.retrieve(transaction_id)
        return response
    
    def get_payment_url(self):
        return self.__payment_url
    
    def get_transaction_id(self):
        return self.__transaction_id

    def get_payment_intent(self,transaction_id):
        response = stripe.checkout.Session.retrieve(transaction_id)
        return response.payment_intent
    
    def get_charge_id(self,payment_intent):
        response = stripe.Charge.list(payment_intent=payment_intent)
        return response.data[0].id

    def create_refund(self,charge_id):
        stripe.Refund.create(charge=charge_id)
        return "gele puluvu"