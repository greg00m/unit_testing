#!/usr/bin/python3


class ThatsEnoughSlices(Exception):
    pass

#@dataclass
class Pizza:
    area: float
    toppings: list

#@dataclass
class SlicedPizza:
    area: float
    toppings: list
    slice_areas: list

def slice_pizza(pizza: Pizza, min_share_of_pie: float, n_cuts: int):
    """Transforms a Pizza object into a SlicedPizza object by calculating the area of slices.

    The pizza is cut n_cut times. Each cut is a line that goes through the center of the circular pizza
    to devide the pizza into n_cuts*2 slices.
    :param pizza: pizza to be sliced
    :param min_share_of_pie: ratio of the min largest slice size / total pizza area
    :param n_cuts: number of slices to cut the pizza into
    :returns: SlicedPizza object
    """
    if n_cuts < 0:
        raise ValueError("Number of cuts must be a non-negative integer.")

    if n_cuts == 0:
        return SlicedPizza(pizza.area, pizza.toppings, slice_areas=[pizza.area])
    n_slices = n_cuts * 2
    slice_areas = [pizza.area/n_slices for n in range(n_slices)]

    if max(slice_areas) < (min_share_of_pie * pizza.area):
        raise ThatsEnoughSlices("Largest pizza slice is smaller than the smallest acceptable slice size.")

    return SlicedPizza(pizza.area, pizza.toppings, slice_areas=slice_areas)
