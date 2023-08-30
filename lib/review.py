# creating a class for the work
class Review:
    all_review = []
    #keeps track af customers review
    def __init__(self, customer: str, restaurant: str, rating: (int, float)):
        self._customer = customer
        self ._restaurant = restaurant
        self._rating = rating
        Review.all_review.append(self)
    # returning the rating
    def rating(self):
        return self._rating
    # returns the customer
    def customer(self):
        return self._customer
    # returns the restaurant
    def restaurant(self):
        return self._restaurant
    #  returns a list of all reviews
    @classmethod
    def all(cls):
        return cls.all_review
    
    def __repr__(self):
        return f"{self._customer}, {self._restaurant}, {self._rating}"


review1= Review("austin mbogo", "highlands", 3)
review2= Review("John mbogo", "lowlands", 2)

print(review1.all())
