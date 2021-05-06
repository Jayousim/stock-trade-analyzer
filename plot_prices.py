import loadData
import numpy as np
import matplotlib.pyplot as plt


def prepare_data(file = 'candidate-home-task-1.2.0/data.json'):
    data_file = file

    assets_data = loadData.ExtractData(data_file)

    return assets_data


def get_asset_effective_price(ask, bid):
    return (ask + bid) / 2


def evaluate_effictive(item):
    return get_asset_effective_price(item['ask'], item['bid'])


def plot_data(assets_data):
    vee = np.vectorize(evaluate_effictive)
    assets_timeline = assets_data.get_rows()
    all_prices = []

    for timeline in assets_timeline:
        asset_avg_prices = timeline
        asset_avg_prices = vee(asset_avg_prices)
        all_prices.append(asset_avg_prices)
    time_stamps = loadData.ExtractData.normalize_times(assets_data.get_columns_names())
    plt.plot(time_stamps, all_prices[0], time_stamps, all_prices[1])
    plt.show()


def plot_prices():
    assets_data = prepare_data()

    plot_data(assets_data)





