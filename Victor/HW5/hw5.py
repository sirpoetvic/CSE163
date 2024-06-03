"""
Victor Wong
CSE163 Data Science
HW5 file
"""

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


def main():
    state_data = load_in_data(
        "food_access/washington.json", "food_access/food_access.csv"
    )
    plot_low_access_tracts(state_data)


def load_in_data(
    wa_census_dataset: str, food_access_dataset: str
) -> gpd.GeoDataFrame:
    """
    merges census_dataset and food_access_dataset, returning
    the result as a GeoDataFrame

    Args:
        census_dataset (str): path to census dataset file
        food_access_dataset (str): path to the food access dataset file

    Returns:
        gpd.GeoDataFrame: Merged GeoDataFrame
    """
    # read the files
    census = gpd.read_file(wa_census_dataset)
    food_access = pd.read_csv(food_access_dataset, index_col=0)

    # return the files, merged on "CTIFP00" and "CensusTract"
    merged = census.merge(
        food_access,
        left_on="CTIDFP00",
        right_on="CensusTract",
        how="left",
    )
    return merged


def percentage_food_data(data: pd.DataFrame):
    """
    Returns the percentage of census tracts in Washington for which we have food access data

    Args:
        data (_type_): _description_
    """

    total_census_tracts = len(data)

    # Number of census tracts with food access data
    tracts_with_food_data = data["CensusTract"].isna().sum()

    # Calculate the percentage
    percentage = (
        (total_census_tracts - tracts_with_food_data) / total_census_tracts
    ) * 100
    return percentage


def plot_map(data):
    """
    plot the shapes of all the census tracts in Washington state

    Args:
        data (pd.DataFrame): merged data of wa census and food_census
    """
    data.plot()
    plt.title("Washington State")
    plt.savefig("map.png", bbox_inches="tight")


def plot_population_map(data):
    """
    plot the census on top of the background of all counties in the census

    Args:
        data (pd.DataFrame): merged data of wa census and food_census
    """
    data = data[["CensusTract", "POP2010", "geometry"]]
    fig, ax = plt.subplots(1)
    # plot background color
    data.plot(ax=ax, color="#EEEEEE")
    # plot population & census tract on top
    data.plot(ax=ax, column="POP2010", legend=True)
    # name the figure
    plt.title("Washington Census Tract Populations")
    # save the figure
    plt.savefig("population_map.png")


def plot_population_county_map(data):
    data = data[["CensusTract", "POP2010", "geometry", "County"]]
    fig, ax = plt.subplots(1)
    # plot background color
    data.plot(ax=ax, color="#EEEEEE")

    # aggregate & graph
    data = data.dissolve(by="County", aggfunc="sum")
    data.plot(ax=ax, column="POP2010", legend=True)
    plt.title("Washington County Populations")
    plt.savefig("county_population_map.png")


def plot_food_access_by_county(data):
    """
    produces 4 plots on the same figure showing information about
    food access across income level

    Args:
        data (pd.DataFrame): merged data of wa census and food_census
    """
    data = data[
        [
            "County",
            "geometry",
            "POP2010",
            "lapophalf",
            "lapop10",
            "lalowihalf",
            "lalowi10",
        ]
    ]
    # dissolve by county
    data = data.dissolve(by="County", aggfunc="sum")

    # ratios (per county, after dissolve) of num people in
    # subcategories to population
    data["lapohalf_ratio"] = data["lapophalf"] / data["POP2010"]
    data["lapop10_ratio"] = data["lapop10"] / data["POP2010"]
    data["lalowihalf_ratio"] = data["lalowihalf"] / data["POP2010"]
    data["lalowi10_ratio"] = data["lalowi10"] / data["POP2010"]

    # creating the subplots
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))
    # plotting backgrounds for all subplots
    data.plot(ax=ax1, color="#EEEEEE")
    data.plot(ax=ax2, color="#EEEEEE")
    data.plot(ax=ax3, color="#EEEEEE")
    data.plot(ax=ax4, color="#EEEEEE")

    # setting scale (vmin and vmax) and enabling legend
    # plotting the respective ratios in their subplots
    data.plot(ax=ax1, column="lapohalf_ratio", vmin=0, vmax=1, legend=True)
    data.plot(ax=ax2, column="lalowihalf_ratio", vmin=0, vmax=1, legend=True)
    data.plot(ax=ax3, column="lapop10_ratio", vmin=0, vmax=1, legend=True)
    data.plot(ax=ax4, column="lalowi10_ratio", vmin=0, vmax=1, legend=True)

    # set titles to each subplot
    ax1.set_title("Low Access: Half")
    ax2.set_title("Low Access + Low Income: Half")
    ax3.set_title("Low Access: 10")
    ax4.set_title("Low Access + Low Income: 10")

    # save figure
    plt.savefig("county_food_access.png")


def plot_low_access_tracts(data):
    """
    plots all census tracts considered "low access" in a file

    Args:
        data (pd.DataFrame): merged data of wa census and food_census
    """
    data = data[
        ["Urban", "Rural", "POP2010", "lapophalf", "lapop10", "geometry"]
    ]
    # check if the population that is considered low access takes at least 33%
    # of the whole population
    is_min_33_p_urban = (1 / 3) <= (data["lapophalf"] / data["POP2010"])
    is_min_33_p_rural = (1 / 3) <= (data["lapop10"] / data["POP2010"])
    # verifies that the urban/rural population reaches threshold
    urban = (data["Urban"] == 1) & (
        (data["lapophalf"] >= 500) | is_min_33_p_urban
    )
    rural = (data["Rural"] == 1) & (
        (data["lapop10"] >= 500) | is_min_33_p_rural
    )

    low_access = data[urban | rural]

    # plotting
    fig, ax = plt.subplots(1)
    # plot background color
    data.plot(ax=ax, color="#EEEEEE")
    # plot all census tracts we have food access data for
    data.dropna().plot(ax=ax, color="#AAAAAA")
    # plotting census tracts under low access
    low_access.plot(ax=ax)
    # name figure
    plt.title("Washington County Populations")
    # save figure
    plt.savefig("low_access.png")


main()
