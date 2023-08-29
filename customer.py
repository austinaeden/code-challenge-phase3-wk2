from review import Review
class Customer:
    all_customers = []

    def __init__(self, given_name=None,  family_name=None):
        self._given_name = given_name
        self._family_name = family_name
        self._full_name = f"{given_name} {family_name}"
        Customer.all_customers.append(self)
    
    def given_name(self):
        return self._given_name
    
    def set_given_name(self, first_name):
        if isinstance(first_name, str):
            self._given_name = first_name
            self._full_name = f"{first_name} {self._family_name}"
        else:
            print (f"ERROR: {first_name} must be a string.")
    
    given_name = property(given_name, set_given_name)


    def family_name(self):
        return self._family_name
    
    def set_family_name(self, last_name):
        if isinstance (last_name, str):
            self._family_name = last_name
            self._full_name = f"{self._given_name} {last_name}"
        else:
            print (f"ERROR: {last_name} must be a string.")
    
    family_name = property(family_name, set_family_name)

    @classmethod
    def all(cls):
        return cls.all_customers
    
    def restaurants(self):
        return set([review.restaurant() for review in Review.all() if review.customer() in self.full_name()])
    
    def add_review(self, restaurant, rating):
        Review(Customer.full_name(self), restaurant, rating)