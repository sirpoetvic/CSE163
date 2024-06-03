import geopandas as gpd
import matplotlib.pyplot as plt


def main():

    all_countries = gpd.read_file('geo_data/ne_110m_admin_0_countries.shp')

    fig, [ax1, ax2, ax3] = plt.subplots(3)

    # top plot
    all_countries.plot(ax=ax1,
                       column="POP_EST",
                       legend=True)

    # middle plot
    sub_region = all_countries.dissolve(by='SUBREGION', aggfunc='sum')
    sub_region.plot(ax=ax2,
                    column='POP_EST',
                    legend=True)

    # bottom plot
    continent = all_countries.dissolve(by='CONTINENT', aggfunc='sum')
    continent.plot(ax=ax3,
                   column='POP_EST',
                   legend=True)

    # plt.show()
    plt.savefig("populations.png")


if __name__ == "__main__":
    main()
