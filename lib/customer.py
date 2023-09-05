# importing review class
from review import Review

class Customer:
    #keeping track of all instances
    all_customers = []
    # initialising the names such that they can be updated
    def __init__(self, given_name=None,  family_name=None):
        self._given_name = given_name
        self._family_name = family_name
        self._full_name = f"{given_name} {family_name}"
        Customer.all_customers.append(self)
    # gets the recently updated name
    def given_name(self):
        return self._given_name
    # updates name only when its a string
    def set_given_name(self, first_name):
        if isinstance(first_name, str):
            self._given_name = first_name
            self._full_name = f"{first_name} {self._family_name}"
        else:
            print (f"ERROR: {first_name} must be a string.")
    
    given_name = property(given_name, set_given_name)

    # gets the recently updated name
    def family_name(self):
        return self._family_name
    # updates name only when its a string
    def set_family_name(self, last_name):
        if isinstance (last_name, str):
            self._family_name = last_name
            self._full_name = f"{self._given_name} {last_name}"
        else:
            print (f"ERROR: {last_name} must be a string.")
    
    family_name = property(family_name, set_family_name)
    # returns all customers
    def full_name(self):
        return self._full_name
    # returns all customers
    @classmethod
    def all(cls):
        return cls.all_customers
    # returns a list of restaurants customer has reviewed
    def restaurants(self):
        return set([review.restaurant() for review in Review.all() if review.customer() in self.full_name()])
    # enables customers to add a nes review
    def add_review(self, restaurant, rating):
        Review(Customer.full_name(self), restaurant, rating)
    # finds any customer in the list
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
            else:
                print("customer cannot be found")
    # finds customer by the given name
    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in Customer.all() if customer.given_name == name]
    
    def __repr__(self):
        return f"{self._given_name} {self._family_name}"
    

# customer1= Customer("austin","mbogo")
# customer2= Customer("John","mbogo")

# print(Customer.find_by_name("austin mbogo"))
# print(Customer.find_all_by_given_name("John"))