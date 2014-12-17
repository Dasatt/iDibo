__author__ = 'satope'

"""The program is suppose  to find the overall cost of a meal including tax and tip"""

meal = 44.50
tax = 0.0675
tip = 0.15

meal += meal*tax
total = meal + (meal*tip)

print("Total is %.2f" %total)
