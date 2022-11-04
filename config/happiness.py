def happiness_function(hours: float, beers: float) -> float:
    return (
        952
        + (hours * beers)
        - (beers**2)
        - (1.5 * (hours**2))
        + (28 * hours)
        + (7 * beers)
    )


FUNCTION = happiness_function

X_RANGE_MIN = 0
X_RANGE_MAX = 24

Y_RANGE_MIN = 0
Y_RANGE_MAX = 24

X_LABEL = "Hours"
Y_LABEL = "Beers"
Z_LABEL = "Happiness"
