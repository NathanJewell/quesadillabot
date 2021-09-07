from PaymentProcessor import PaymentProcessor
from OrderManager import OrderManager

def do_quesadillabot():
    om = OrderManager()
    om.start_manager()
    

if __name__ == "__main__":
    do_quesadillabot()