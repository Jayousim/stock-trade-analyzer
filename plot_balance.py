import loadData
import plot_prices

def prepare_data():
    trader1_data_file = 'candidate-home-task-1.2.0/tradesAS_test.json'
    trader2_data_file = 'candidate-home-task-1.2.0/tradesAO_test.json'
    assets_prices = plot_prices.prepare_data('candidate-home-task-1.2.0/data_test.json')
    trader1_data = loadData.ExtractData(trader1_data_file)
    trader2_data = loadData.ExtractData(trader2_data_file)
    return trader1_data, trader2_data, assets_prices


def analyze_data(trader1_data, trader2_data, assets_data):
    timeline = assets_data.get_df()
    for _, record in trader1_data.get_iterrows():
        print(timeline[record['time']]) ## check key error
        record['actions']

    for action in trader2_data.get_columns():
        print(action)


a = prepare_data()
analyze_data(*a)
