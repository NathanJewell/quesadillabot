class PaymentException(Exception):
    pass

class Payment:
    def __init__(self, email_uid, date, description, amount):
        self.email_uid = email_uid
        self.date = date
        self.amount = float(amount)
        self.description = description
        

        



#description format....
# QB: <flour/corn/bread> <order in future> <cook time multiplier> <cheese multiplier>