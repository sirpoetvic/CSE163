import geopandas as gpd  # noqa: F401
import matplotlib.pyplot as plt


def create_south_america_png():
    countries = gpd.read_file("geo_data/ne_110m_admin_0_countries.shp")
    south_america = countries[countries["CONTINENT"] == "South America"]

    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    south_america.plot(
        column="POP_EST",
        legend=True,
        legend_kwds={
            "label": "Population by Country",
            "orientation": "vertical",
        },
        ax=ax,
    )
    ax.set_title("Population of South American Countries", fontsize=15)
    plt.savefig("south_america.png")


def create_small_and_rich_png():
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
        legend_kwds={
            "label": "GDP (in million USD)",
            "orientation": "vertical",
        },
        ax=ax,
    )
    plt.savefig("small_and_rich.png")


def create_populations_png():
    # Your code goes here!
    pass


def main():
    create_south_america_png()
    create_small_and_rich_png()
    create_populations_png()


if __name__ == "__main__":
    main()
