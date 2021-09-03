class PaymentException(Exception):
    pass

class Payment:
    def __init__(self, email_uid, date, description, amount):
        self.email_uid = email_uid
        self.date = date
        self.amount = float(amount)
        self.extract_order(description)
        

    def extract_order(self, description):
        self.order_data = description.split(' ')



#description format....
# QB: <flour/corn/bread> <order in future> <cook time multiplier> <cheese multiplier>