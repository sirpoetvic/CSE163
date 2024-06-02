# student name


from re import L
import geopandas as gpd


def main():
    state_data = load_in_data(
        "food_access/washington.json", "food_access/food_access.csv"
    )
    # print(percentage_food_data(state_data))
    # plot_map(state_data)
    # plot_population_map(state_data)
    # plot_population_county_map(state_data)
    # plot_food_access_by_county(state_data)
    # plot_low_access_tracts(state_data)
    pass


def load_in_data(census_dataset: str, food_access_dataset: str):
    """
    merges census_dataset and food_access_dataset, returning
    the result as a GeoDataFrame

    Args:
        census_dataset (str): census dataset
        food_access_dataset (str): food access dataset
    """
    zipped_folder = zip(census_dataset, food_access_dataset)
    return zipped_folder


def percentage_food_data(data):
    pass


def plot_map(data):
    pass


def plot_population_map(data):
    pass


def plot_population_county_map(data):
    pass


def plot_low_access_tracts(data):
    pass


if __name__ == "__main__":
    main()
