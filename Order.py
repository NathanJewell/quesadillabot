class OrderException(Exception):
    pass 

class Order:

    def __init__(self, payment):
        self.recieved_time = payment.date
        self.email_uid = payment.email_uid
        self.payment_amount = payment.amount
        self.valid_order = 

        self.order_details = {
            "type" : "",
            "delay" : 0,
            "cook" : 1,
            "cheese" : 1
        }

        self.extract_order(payment.description)

    def extract_order(self, description):
        self.order_data = description.split(' ')
        if self.order_data[0] == "QB:":
            self.order_details["type"] = self.order_data[1]
            self.order_details["delay"] = self.order_data[2] if 
            self.order_details["cook_multiplier"] = self.order_data[3]
        else:
            raise OrderException("Payment description could not be parsed as an order.")

    def get_order_price(self):
        return self.payment.amount

    def get_order_uid(self):
        return self.payment.email_uid

    def is_valid()

