import loadData
import plot_prices


def prepare_data():
    trader1_data_file = 'candidate-home-task-1.2.0/tradesAS_test.json'
    trader2_data_file = 'candidate-home-task-1.2.0/tradesAO_test.json'
    assets_prices = plot_prices.prepare_data('candidate-home-task-1.2.0/data_test.json')
    trader1_data = loadData.ExtractData(trader1_data_file)
    trader2_data = loadData.ExtractData(trader2_data_file)
    return trader1_data, trader2_data, assets_prices


def action_effect(action_string, prices):
    if action_string == "sellA":
        return prices["assetA"]["bid"]

    elif action_string == "buyA":
        return -prices["assetA"]["ask"]

    elif action_string == "sellB":
        return prices["assetB"]["bid"]

    elif action_string == "buyB":
        return -prices["assetB"]["ask"]

def analyze_data(trader1_data, trader2_data, assets_data):
    timeline = assets_data.get_df()
    trader1_balance = 0
    trader2_balance = 0

    for _, record in trader1_data.get_iterrows():
        prices = timeline[record['time']]  ## check key error
        for action in record['actions']:
            trader1_balance += action_effect(action, prices)
    return trader1_balance

    # for action in trader2_data.get_columns():
    #     print(action)


a = prepare_data()
res = analyze_data(*a)
print(res)
