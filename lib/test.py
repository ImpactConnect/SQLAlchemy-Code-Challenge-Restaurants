from database import SessionLocal, init_db
from models import Customer, Restaurant, Review

# Initialize the database
init_db()

# Sample usage of the methods
session = SessionLocal()

# Create a customer
new_customer = Customer(first_name="John", last_name="Doe")
session.add(new_customer)
session.commit()

# Create a restaurant
new_restaurant = Restaurant(name="Sample Restaurant", price=50.0)
session.add(new_restaurant)
session.commit()

# Add a review
new_review = Review(customer_id=new_customer.id, restaurant_id=new_restaurant.id, star_rating=5)
session.add(new_review)
session.commit()

# Test the methods
customer_instance = session.query(Customer).first()
print(customer_instance.full_name())  # Output: John Doe

restaurant_instance = session.query(Restaurant).first()
print(restaurant_instance.fanciest().name)  # Output: Sample Restaurant

review_instance = session.query(Review).first()
print(review_instance.full_review())  # Output: Review for Sample Restaurant by John Doe: 5 stars.
