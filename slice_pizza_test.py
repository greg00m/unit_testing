#!/usr/bin/python3

import pytest
import slice_pizza

# when running slice_pizza.py: NameError: name 'dataclass' is not defined, use "import dataclass"

#This function tests if the entered data is of the correct data type required by the program

def variable_test(area: float, toppings: list, slice_areas: list, min_share_of_pie: float, n_cuts: int):

	assert type(area) is float, "The area must contain a decimal, ex: 2.0."
	print ("The area of the pizza is: ",area)
	assert type(min_share_of_pie) is float, "The minimal share of pie must contain."
	print ("The minimal share of pie is: ",min_share_of_pie)
	assert type(n_cuts) is int, "The number of cuts cannot have a decimal point."
	print ("The number of cuts is: ",n_cuts)

	assert toppings is True, "There must be a list of toppings on the pizza."
	print ("The list of toppings is: ",toppings)
	assert slice_areas is True, "There must be a list of slice areas."
	print ("This is a list of slice areas",slice_areas)

