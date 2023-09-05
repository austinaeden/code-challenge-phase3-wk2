import unittest
from review import Review


class TestReview(unittest.TestCase):

    def test_init(self):
        review = Review("austin mbogo", "highlands", 3)
        self.assertEqual(review.customer(), "austin mbogo")
        self.assertEqual(review.restaurant(), "highlands")
        self.assertEqual(review.rating(), 3)

    def test_all(self):
        review1 = Review("austin mbogo", "highlands", 3)
        review2 = Review("John mbogo", "lowlands", 2)
        self.assertEqual(Review.all(), [review1, review2])

    def test_repr(self):
        review = Review("austin mbogo", "highlands", 3)
        self.assertEqual(repr(review), "austin mbogo, highlands, 3")


if __name__ == "__main__":
    unittest.main()

import unittest
from review import Review

class TestRestaurant(unittest.TestCase):

    def test_import_review(self):
        from review import Review
        self.assertTrue(Review)

if __name__ == '__main__':
    unittest.main()

import unittest
from review import Review
from customer import Customer

class TestRestaurant(unittest.TestCase):

    def test_import_review(self):
        from review import Review
        self.assertTrue(Review)

    def test_import_customer(self):
        from customer import Customer
        self.assertTrue(Customer)

    def test_all_customers(self):
        # create a few customers
        customer1 = Customer("John", "Doe")
        customer2 = Customer("Jane", "Doe")
        customer3 = Customer("Bob", "Smith")

        # check that all_customers contains all the customers
        self.assertEqual(Customer.all(), [customer1, customer2, customer3])

if __name__ == '__main__':
    unittest.main()
   