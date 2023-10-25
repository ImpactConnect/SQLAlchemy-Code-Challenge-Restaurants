# Restaurant Reviews Project

This project demonstrates a basic implementation of a restaurant review system using Python and SQLAlchemy. It includes classes for `Customer`, `Restaurant`, and `Review`, allowing users to create customers, restaurants, and reviews, and perform various operations related to them.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.6 or higher)
- SQLAlchemy

You can install SQLAlchemy using the following command:

```
pip install sqlalchemy
```

## Project Structure

The project has the following file structure:

- `models.py`: Contains the class definitions for Customer, Restaurant, and Review.
- `database.py`: Handles database setup and connection using SQLAlchemy.
- `test.py`: A script for testing the implemented methods.
- `mydatabase.db`: SQLite database file where data is stored.

## Usage

1. **Database Initialization:**

   Before running the project, initialize the database by executing the following command:

   ```
   python database.py
   ```

   This command will create the SQLite database file `mydatabase.db` with the necessary tables.

2. **Testing the Implemented Methods:**

   Run the `test.py` script to test the implemented methods:

   ```
   python debug.py
   ```

   This script performs various operations like creating customers, restaurants, and reviews, and then tests the implemented methods like `full_name()`, `fanciest()`, `favorite_restaurant()`, and others.

## Class Methods

### Customer Class:

- `full_name()`: Returns the full name of the customer, concatenating first name and last name.
- `favorite_restaurant(session)`: Returns the restaurant instance that has the highest star rating from this customer.
- `add_review(restaurant, rating, session)`: Creates a new review for the given restaurant with the specified rating.
- `delete_reviews(restaurant, session)`: Removes all reviews for the given restaurant associated with this customer.

### Restaurant Class:

- `fanciest(session)`: Returns one restaurant instance for the restaurant that has the highest price.
- `all_reviews(session)`: Returns a list of strings with all the reviews for this restaurant formatted as specified.

### Review Class:

- `full_review()`: Returns a formatted string containing the restaurant name, customer's full name, and review star rating.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

