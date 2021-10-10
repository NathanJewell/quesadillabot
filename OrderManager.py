from Order import Order, OrderException
import PaymentProcessor, PaymentProcessorException

class OrderManager:

    def __init__(self):
        self.order_queue = []
        self.stop_signal = True

        self.payment_processor = PaymentProcessor()

    def organize_queue(self):
        self.order_queue = sorted(self.order_queue, key=lambda o: o.time_recieved)

    def start_manager(self):
        self.stop_signal = False
        while not self.stop_signal:
            new_payments = self.payment_processor.get_new_payments()
            for payment in new_payments:
                try:
                    self.order_queue.append(Order(payment))
                except OrderException as e:
                    
            new_orders = [Order(p) for p in new_payments]
            self.order_queue += new_orders
            self.organize_queue()


