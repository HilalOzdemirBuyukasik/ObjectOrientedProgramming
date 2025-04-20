
#Create a PaymentMethod class.

#Define a pay() method inside this class.

#Then, create three subclasses: CreditCardPayment, PayPalPayment, and CryptoPayment, and override the pay() method in each subclass to reflect their specific behavior.

#Finally, loop through all these classes in a single list and demonstrate how each one works by calling their respective pay() method.

class PaymentMethod:
    def pay(self, amount):
        print(f' {amount} TL has been paid.')

class CreditCardPayment(PaymentMethod):
    def pay(self,amount):
        print(f'{amount} TL has been paid using a credit card.')

class PayPalPayment(PaymentMethod):
    def pay(self,amount):
        print(f'{amount} TL has been paid via PayPal.')

class CryptoPayment(PaymentMethod):
    def pay(self,amount):
        print(f'{amount} TL has been paid using cryptocurrency.')


payments = [CreditCardPayment(),
            PayPalPayment(),
            CryptoPayment()]

for method in payments:
    method.pay(250)