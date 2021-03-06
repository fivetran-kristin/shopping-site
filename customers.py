"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self,
                 first_name, 
                 last_name, 
                 email, 
                 password,
                 ):
        self.first_name = first_name
        self.last_name = last_name,
        self.email = email,
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customers in console."""
        return "<Customer: {} {} {} {}>".format(self.first_name, self.last_name, self.email, self.password)

def read_customers_from_file_path(filepath):
    """Read customer type data and populate dictionary with customer objects 
    
    Dictionary keys will be email address, with a value of a dictionary of customer attributes."""

    customers = {}

    with open(filepath) as file:
        for line in file:
            (first_name, 
            last_name,
            email,
            password) = line.strip().split("|")

            customers[email] = Customer(first_name, 
                                        last_name, 
                                        email, 
                                        password)
    return customers

customers = read_customers_from_file_path("customers.txt")

def get_by_email(email):
    """ Returns a list of customers, by email"""

    return customers[email]

