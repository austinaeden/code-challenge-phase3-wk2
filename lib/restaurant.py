# imports review from the review file
from review import Review
class Restaurant:
    # initialises the name of the restaurant 
    def __init__(self, name: str):
        self._name= name
    # returns the name of the restaurant 
    def name(self):
        return self._name
    # returns a list of restaurant reviews
    def reviews (self):
        return [review for review in Review.all() if review.restaurant()== self._name]        
    # returns a list of customers 
    def customers(self):
        return set([review.customer() for review in  self.reviews()])
    # calculates the average rating star 
    def average_rating(self):
        if not self.reviews():
            return 0  
        total_ratings = sum(review.rating() for review in self.reviews())
        average = total_ratings / len(self.reviews())
        return average
    

# restaurant1= Restaurant("highlands")
# restaurant2= Restaurant("lowlands")

# print(restaurant1.average_rating())
# print(restaurant2.average_rating())