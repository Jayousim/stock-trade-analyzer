import loadData
import plot_prices
import matplotlib.pyplot as plt
import matplotlib.dates


def prepare_data(trader1_data_file = 'candidate-home-task-1.2.0/tradesAS.json',
                 trader2_data_file = 'candidate-home-task-1.2.0/tradesAO.json', assets_data = 'candidate-home-task-1.2.0/data.json'):

    assets_prices = plot_prices.prepare_data(assets_data)
    trader1_data = loadData.ExtractData(trader1_data_file)
    trader2_data = loadData.ExtractData(trader2_data_file)
    return trader1_data, trader2_data, assets_prices


def action_effect(action_string, prices, trader_assetA_balance, trader_assetB_balance):
    if action_string == "sellA":
        trader_assetA_balance[-1] -= 1
        return prices["assetA"]["bid"]

    elif action_string == "buyA":
        trader_assetA_balance[-1] += 1
        return -prices["assetA"]["ask"]

    elif action_string == "sellB":
        trader_assetB_balance[-1] -= 1
        return prices["assetB"]["bid"]

    elif action_string == "buyB":
        trader_assetB_balance[-1] += 1
        return -prices["assetB"]["ask"]


def get_balance_track(assets_data, trader_data):
    trader_assetA_balance = []
    trader_assetB_balance = []
    trader_money_balance = 0
    trader_balance = []
    timeline = []
    for _, record in trader_data.get_iterrows():
        timeline.append(record['time'])
        prices = assets_data[record['time']]  ## check key error
        asset1_amount = 0 if len(trader_assetA_balance) == 0 else trader_assetA_balance[-1]
        asset2_amount = 0 if len(trader_assetB_balance) == 0 else trader_assetB_balance[-1]
        trader_assetA_balance.append(asset1_amount)
        trader_assetB_balance.append(asset2_amount)
        for action in record['actions']:
            trader_money_balance += action_effect(action, prices,trader_assetA_balance, trader_assetB_balance)

        trader_balance.append(trader_money_balance)

    return trader_balance, timeline, trader_assetA_balance, trader_assetB_balance


def analyze_data(trader1_data, trader2_data, assets_data):
    timeline = assets_data.get_df()

    trader1_balance_timeline = get_balance_track(timeline, trader1_data)
    trader2_balance_timeline = get_balance_track(timeline, trader2_data)
    return trader1_balance_timeline, trader2_balance_timeline


def plot_balance_data():

    a = prepare_data()
    res = analyze_data(*a)

    fig, axs = plt.subplots(2, 2)

    trader1_times = res[0][1] #matplotlib.dates.date2num(res[0][1])
    trader2_times = res[1][1] #matplotlib.dates.date2num(res[0][1])
    axs[0, 0].plot(trader1_times, res[0][0])
    axs[0, 1].plot(trader2_times, res[1][0])
    axs[1, 0].plot(trader1_times, res[0][2], trader1_times, res[0][3])
    axs[1, 1].plot(trader2_times, res[1][2], trader2_times, res[1][3])
    plt.show()


