from lib.review import Review
class Restaurant:

    def __init__(self, name: str):
        self._name= name

    def name(self):
        return self._name
    
    def reviews (self):
        return [review for review in Review.all() if review.restaurant()== self._name]        


    def customers(self):
        return set([review.customer() for review in  self.reviews()])
    

    def average_rating(self):
        if not self.reviews():
            return 0  
        total_ratings = sum(review.rating() for review in self.reviews())
        average = total_ratings / len(self.reviews())
        return average