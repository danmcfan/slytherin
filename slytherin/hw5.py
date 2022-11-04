import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import pyplot as plt


def plot_happiness_3d() -> None:
    def happiness(hours: float, beers: float) -> float:
        return (
            952
            + (hours * beers)
            - (beers**2)
            - (1.5 * (hours**2))
            + (28 * hours)
            + (7 * beers)
        )

    hours_range = np.arange(0, 24, 0.1)
    beers_range = np.arange(0, 24, 0.1)

    hours_grid, beers_grid = np.meshgrid(hours_range, beers_range)

    happiness_grid = happiness(hours_grid, beers_grid)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    surface = ax.plot_surface(
        hours_grid,
        beers_grid,
        happiness_grid,
        rstride=1,
        cstride=1,
        cmap=cm.RdBu,
        linewidth=0,
        antialiased=False,
    )

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))

    fig.colorbar(surface, shrink=0.5, aspect=5)

    plt.show()
