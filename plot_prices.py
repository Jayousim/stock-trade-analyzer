import loadData
import numpy as np

extracted_data = loadData.extractData('candidate-home-task-1.2.0/data_test.json')
assets_timeline = extracted_data.get_rows()


def get_asset_effective_price(ask, bid):
    return (ask + bid) / 2


def evaluate_effictive(item):
    return get_asset_effective_price(item['ask'], item['bid'])
vee = np.vectorize(evaluate_effictive)



all_prices = []
for timeline in assets_timeline:
    asset_avg_prices = timeline
    asset_avg_prices = vee(asset_avg_prices)
    # for record in timeline:
    #     effective_price = get_asset_effective_price(record['ask'], record['bid'])
    #     asset_avg_prices.append(effective_price)
    all_prices.append(asset_avg_prices)

print(np.array(all_prices))


