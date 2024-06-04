from itertools import count
import geopandas as gpd  # noqa: F401
import pandas as pd
import matplotlib.pyplot as plt


def create_south_america_png():
    """
    Makes a plot of the countries in South America, colored
    by their population
    """
    # Load the data
    countries = gpd.read_file("geo_data/ne_110m_admin_0_countries.shp")

    # Filter for South America
    south_america = countries[countries["CONTINENT"] == "South America"]

    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    # Create the plot
    ax = south_america.plot(
        column="POP_EST",
        legend=True,
        legend_kwds={
            "label": "Population by Country",
            "orientation": "vertical",
        },
        ax=ax,
    )

    # Set the title
    ax.set_title("Population of South American Countries", fontsize=15)

    # Save the figure
    plt.savefig("south_america.png")


def create_small_and_rich_png():
    """
    Makes a plot of the world highlighting countries that are "small and rich"
    Country is rich if its GDP is at least 500,000
    Country is small if the population is at most 80,000,000
    """
    countries = gpd.read_file("geo_data/ne_110m_admin_0_countries.shp")

    # Country considered rich if the GDP is greater than 500,000
    rich = countries["GDP_MD_EST"] >= 500000

    # Country considered small if the popoulation is less than 80,000,000
    small = countries["POP_EST"] < 80000000
    small_and_rich = countries[small & rich]

    # figsize 15, 7 for legibility
    fig, ax = plt.subplots(1, 1, figsize=(15, 7))
    countries.plot(color="#EEEEEE", ax=ax)
    small_and_rich.plot(
        column="GDP_MD_EST",
        legend=True,
        ax=ax,
    )

    # Save figure
    plt.savefig("small_and_rich.png")


def create_populations_png():
    """
    Plots 3 axes in one figure:
    First axis: Plots population by country
    Second axis: Plots population aggregated by subregion
    Third axis: Plots population aggregated by continent
    """
    countries = gpd.read_file("geo_data/ne_110m_admin_0_countries.shp")

    # Filter down to just the columns of interest
    populations = countries[["POP_EST", "CONTINENT", "SUBREGION", "geometry"]]
    # 3 plots
    fig, [ax1, ax2, ax3] = plt.subplots(3)

    # Dissolve by desired area (subregion or continent)
    populations_subregion = populations.dissolve(by="SUBREGION", aggfunc="sum")
    populations_continent = populations.dissolve(by="CONTINENT", aggfunc="sum")

    # Plotting regular (just by country)
    populations.plot(column="POP_EST", legend=True, ax=ax1)

    # Plotting other dissolved data
    populations_subregion.plot(column="POP_EST", legend=True, ax=ax2)
    populations_continent.plot(column="POP_EST", legend=True, ax=ax3)

    # Save figure
    plt.savefig("populations.png")


def main():
    create_south_america_png()
    create_small_and_rich_png()
    create_populations_png()


if __name__ == "__main__":
    main()
