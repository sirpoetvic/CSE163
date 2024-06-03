import geopandas as gpd
import matplotlib.pyplot as plt


def main():

    all_countries = gpd.read_file('geo_data/ne_110m_admin_0_countries.shp')

    # filters for rich & small
    is_rich = all_countries['GDP_MD_EST'] >= 500000
    is_small = all_countries['POP_EST'] <= 80000000

    all_together = all_countries[is_rich & is_small]

    fig, ax = plt.subplots(1, figsize=(15, 7))

    # plot the grey bg
    all_countries.plot(ax=ax,
                       color="#EEEEEE")

    # plot the filtered data ontop of the same plot
    all_together.plot(ax=ax,
                      column='GDP_MD_EST',
                      legend=True)
    # plt.show()
    plt.savefig('small_and_rich.png')


if __name__ == "__main__":
    main()
