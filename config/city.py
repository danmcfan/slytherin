import math


def city_function(x: float, y: float) -> float:
    return 300 * (math.e ** ((-1 * (x**2)) - (y**2)))


FUNCTION = city_function

CITY_RANGE = 10

X_RANGE_MIN = -CITY_RANGE
X_RANGE_MAX = CITY_RANGE

Y_RANGE_MIN = -CITY_RANGE
Y_RANGE_MAX = CITY_RANGE

X_LABEL = "X"
Y_LABEL = "Y"
Z_LABEL = "Population Density"
