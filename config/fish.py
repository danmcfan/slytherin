def fish_function(x: float, y: float) -> float:
    return 122 - (2 * x) - y + (0.02 * (x**2)) + (0.015 * (y**2)) - (0.01 * x * y)


FUNCTION = fish_function

X_RANGE_MIN = 0
X_RANGE_MAX = 100

Y_RANGE_MIN = 0
Y_RANGE_MAX = 100

X_LABEL = "X"
Y_LABEL = "Y"
Z_LABEL = "Fish"
