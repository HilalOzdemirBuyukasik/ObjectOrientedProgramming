📖 01_class - Class Basics
Description: This exercise introduces the basics of Python classes and object-oriented programming (OOP). It defines a Book class with attributes such as title, author, and year. The class includes methods like __str__() to display book details and is_classic() to check if the book is considered a classic (published before 1970). This exercise helps solidify the understanding of how to create and use classes in Python.

📖 02_init - The __init__ Method
Description: This exercise demonstrates the usage of the __init__() method, which is the constructor in Python classes. The Employee class is introduced, with attributes like name, position, and salary. The class includes methods to display employee information (get_info() and __str__()), apply a salary raise (apply_raise()), and give a bonus (give_bonus()). This exercise emphasizes the importance of the __init__() constructor in initializing object attributes and demonstrates common methods for handling attributes and calculations within a class.

📖 03_inheritance - Class Inheritance
Description: This exercise focuses on class inheritance in Python, demonstrating how to create a base class and extend it with subclasses. The base class Animal is created, with a method make_sound(). The subclasses Dog and Cat inherit from Animal and override the make_sound() method to print specific sounds for each animal. The exercise highlights the power of inheritance in OOP, allowing code reuse and the ability to customize behavior in subclasses.

📖 04_overriding - Method Overriding
Description: This exercise demonstrates method overriding by modeling different payment methods in an online store. A base class PaymentMethod includes a generic pay() method. Three subclasses—CreditCardPayment, PayPalPayment, and CryptoPayment—override the pay() method to reflect their own payment processes. The exercise shows how overriding allows subclasses to provide specific implementations of a shared method, reinforcing the concept of polymorphism in OOP.

📖 05_encapsulation - Bank Account Management with Encapsulation
Description:
This exercise demonstrates the principle of encapsulation in object-oriented programming. A BankAccount class is created to simulate simple banking operations while ensuring that sensitive data (like the balance) is protected and only accessible through controlled methods.

The balance is defined as a private attribute (__balance), and can only be accessed or modified through dedicated getter and setter methods. Additional methods such as deposit(), withdraw(), and transfer() are implemented with proper validation to ensure that all transactions are secure and logically correct.

📖 06_abstraction - Bank Account with Abstraction
Description: This exercise demonstrates the concept of abstraction in Python using an abstract class. An AbstractAccount class is defined with abstract methods such as get_balance(), set_balance(), deposit(), withdraw(), and transfer(). These methods are designed to be implemented in a subclass.
The BankAccount class inherits from AbstractAccount and implements these methods to manage bank account operations like depositing, withdrawing, and transferring funds.
This exercise emphasizes the importance of defining common interfaces using abstract classes while allowing concrete classes to implement the specific functionality. The goal is to demonstrate how abstraction helps in organizing and simplifying complex systems by hiding unnecessary details from the user.
