import assets_money_blanace
import matplotlib.pyplot as plt


def summary_assets(trader1_balance_timeline, assets_data):
    trader_1_times = trader1_balance_timeline[1]
    trader1_pnl = []
    for i, balance in enumerate(trader1_balance_timeline[0]):
        prices = assets_data[trader_1_times[i]]
        net_balance = balance + prices["assetA"]["bid"] * trader1_balance_timeline[2][i]
        net_balance = net_balance + prices["assetB"]["bid"] * trader1_balance_timeline[3][i]
        trader1_pnl.append(net_balance)
    return trader1_pnl


def analyze_data(trader1_data, trader2_data, assets_data):
    timeline = assets_data.get_df()

    trader1_balance_timeline = assets_money_blanace.get_balance_track(timeline, trader1_data)
    trader2_balance_timeline = assets_money_blanace.get_balance_track(timeline, trader2_data)

    trader1_pnl = summary_assets(trader1_balance_timeline, timeline)
    trader2_pnl = summary_assets(trader2_balance_timeline, timeline)

    return trader1_pnl, trader2_pnl, trader1_balance_timeline[1], trader2_balance_timeline[1]


def plot_pnl():
    a = assets_money_blanace.prepare_data()
    trader1_pnl, trader2_pnl, trader1_times, trader2_times = analyze_data(*a)

    fig, axs = plt.subplots(1, 2)
    print(len(trader1_times), len(trader1_pnl))
    print(trader1_times, trader1_pnl)
    axs[0].plot(trader1_times, trader1_pnl)
    #axs[1].plot_date(trader2_times, trader2_pnl)

    plt.show()