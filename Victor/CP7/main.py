import geopandas as gpd  # noqa: F401
import matplotlib.pyplot as plt  # noqa: F401


def create_south_america_png():

    country = gpd.read_file("geo_data/ne_110m_admin_0_countries.shp")
    south_america = country[country["CONTINENT"] == "South America"]

    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    south_america.plot(
        column="POP_EST",
        cmap="viridis",
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
    # Your code goes here!
    pass


def create_populations_png():
    # Your code goes here!
    pass


def main():
    create_south_america_png()
    create_small_and_rich_png()
    create_populations_png()


if __name__ == "__main__":
    main()
