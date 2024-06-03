import geopandas as gpd
import matplotlib.pyplot as plt


def main():

    all_countries = gpd.read_file('geo_data/ne_110m_admin_0_countries.shp')

    south_america = all_countries[
        all_countries['CONTINENT'] == 'South America']

    fig, ax = plt.subplots(1)
    south_america.plot(ax=ax,
                       column='POP_EST',
                       legend=True)

    # plt.show()
    plt.savefig('south_america.png')


if __name__ == "__main__":
    main()
