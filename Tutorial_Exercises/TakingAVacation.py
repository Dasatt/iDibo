__author__ = 'satope'
"""This program helps you to plan a vacation trip
I would also be testing doctest in some of the functions here"""

def hotel_cost(nights):
    """ This function returns the hotels cost. For instance
    >>> hotel_cost(1)
    140
    >>> hotel_cost(3)
    420
    """
    hotels_cost = 140*nights
    return hotels_cost

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
def rental_car_cost(days):
    rent_cost = days *40
    if days >= 7:
        rent_cost -= 50
    elif days >= 3 and days <7:
        rent_cost -= 20
    return rent_cost

def trip_cost(city, days, spending_money):
    cost = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    return cost

print trip_cost("Los Angeles", 4, 600)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
