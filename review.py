class review:
    all_review = []

    def __init__(self, customer: str, restaurant: str, rating: (int, float)):
        self._customer = customer
        self ._restaurant = restaurant
        self._rating = rating
        review.all_review.append(self)
    
    def rating(self):
        return self._rating
    
    def customer(self):
        return self._customer
    
    def restaurant(self):
        return self._restaurant
     
    @classmethod
    def all(cls):
        return cls.all_review
    
    