"""
William Dinh
Intermediate Data Programming
"""

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


def load_in_data(census, food_access):
    """_summary_

    Args:
        census (_type_): _description_
        food_access (_type_): _description_

    Returns:
        _type_: _description_
    """
    census_data = gpd.read_file(census)
    food_access_data = pd.read_csv(food_access)

    merged_data = census_data.merge(food_access_data,
                                    left_on='CTIDFP00',
                                    right_on='CensusTract',
                                    how='left')
    return merged_data


def percentage_food_data(merged):
    """
    Calculates percentage of tracts in WA
    Args:
        merged_dataset (geospatial dataframe):
        contains food access data, merged.

    Returns:
        float: % of census tracts in Washington
        for which we have food access data
    """
    total = len(merged)
    nans = merged["CensusTract"].isna().sum()

    return (total - nans) / total * 100


def plot_map(merged):
    """_summary_

    Args:
        merged (_type_): _description_
    """
    fig, ax = plt.subplots(1)
    merged.plot(ax=ax)
    plt.title("Washington State")
    # plt.show()
    plt.savefig("Washington State")


def plot_population_map(merged):
    """_summary_

    Args:
        merged (_type_): _description_
    """
    merged = merged[["CensusTract", "POP2010", "geometry"]]
    fig, ax = plt.subplots(1)
    # plot bg color, then plot the pop2010 & census tract ontop
    merged.plot(ax=ax,
                color="#EEEEEE")
    merged.plot(ax=ax,
                column="POP2010",
                legend=True)
    plt.title("Washington Census Tract Populations")
    # plt.show()
    plt.savefig("population_map.png")


def plot_population_county_map(merged):
    """_summary_

    Args:
        merged (_type_): _description_
    """
    merge = merged[["CensusTract", "POP2010", "geometry", "County"]]
    fig, ax = plt.subplots(1)

    merge.plot(ax=ax,
               color="#EEEEEE")
    # aggregate
    merge = merge.dissolve(by='County', aggfunc='sum')

    merge.plot(ax=ax,
               column="POP2010",
               legend=True)

    plt.title("Washington County Populations")
    # plt.show()
    plt.savefig("county_population_map.png")


def plot_food_access_by_county(merged):
    """_summary_

    Args:
        merged (_type_): _description_
    """
    merge = merged[["CensusTract",
                    "POP2010",
                    "geometry",
                    "County",
                    "lapophalf",
                    "lapop10",
                    "lalowihalf",
                    "lalowi10"]]

    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2,
                                                 figsize=(20, 10))

    # bg color
    merge.plot(ax=ax1,
               color="#EEEEEE")
    merge.plot(ax=ax2,
               color="#EEEEEE")
    merge.plot(ax=ax3,
               color="#EEEEEE")
    merge.plot(ax=ax4,
               color="#EEEEEE")

    merge = merge.dissolve(by='County', aggfunc='sum')

    merge["lapophalf_ratio"] = merge["lapophalf"] / merge["POP2010"]
    merge["lapop10_ratio"] = merge["lapop10"] / merge["POP2010"]
    merge["lalowihalf_ratio"] = merge["lalowihalf"] / merge["POP2010"]
    merge["lalowi10_ratio"] = merge["lalowi10"] / merge["POP2010"]

    # Low Access Plot
    merge.plot(ax=ax1,
               column="lapophalf_ratio",
               legend=True,
               vmin=0,
               vmax=1)
    ax1.set_title('Low Access: Half')

    # Low 10% Plot
    merge.plot(ax=ax2,
               column="lapop10_ratio",
               legend=True,
               vmin=0,
               vmax=1)
    ax2.set_title('Low Access: 10')

    # Low Access + Low Income
    merge.plot(ax=ax3,
               column="lalowihalf_ratio",
               legend=True,
               vmin=0,
               vmax=1)
    ax3.set_title('Low Access + Low Income')

    # Low Access + Low Income 10
    merge.plot(ax=ax4,
               column="lalowi10_ratio",
               legend=True,
               vmin=0,
               vmax=1)
    ax4.set_title('Low Access + Low Income 10')

    # plt.show()
    plt.savefig("county_food_access.png")


def plot_low_access_tracts(merged):
    """Plot low access census tracts.

    Args:
        merged (geospatial dataframe):
    """
    merge = merged[["Urban",
                    "Rural",
                    "POP2010",
                    "lapophalf",
                    "lapop10",
                    "geometry"]]

    # this is so that urban and rural can compare properly in
    # urban_la and rural_la as i had TypeErrors there.
    urban = merge["Urban"].astype(bool)
    rural = merge["Rural"].astype(bool)

    # Urban filters
    urban_500_ppl = merge["lapophalf"] >= 500
    urban_33_pct = merge["lapophalf"] / merge["POP2010"] >= 0.33
    urban_la = urban & (urban_500_ppl | urban_33_pct)

    # Rural filters
    rural_500_ppl = merge["lapop10"] >= 500
    rural_33_pct = merge["lapop10"] / merge["POP2010"] >= 0.33
    rural_la = rural & (rural_500_ppl | rural_33_pct)

    # Combined filter for low access
    low_access = merge[urban_la | rural_la]

    fig, ax = plt.subplots(1)

    # Layer 1, background
    merge.plot(ax=ax, color="#EEEEEE")

    # Layer 2, where we have food access data
    merge.dropna().plot(ax=ax, color="#AAAAAA")

    # Layer 3, low access food
    low_access.plot(ax=ax)

    plt.title("Low Access Census Tracts")
    # plt.show()
    plt.savefig("low_access.png")


def main():
    state_data = load_in_data(
        'food_access/washington.json',
        'food_access/food_access.csv'
    )
    print(percentage_food_data(state_data))
    plot_map(state_data)
    plot_population_map(state_data)
    plot_population_county_map(state_data)
    plot_food_access_by_county(state_data)
    plot_low_access_tracts(state_data)


if __name__ == '__main__':
    main()
