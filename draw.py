import pickle
import numpy as np
import matplotlib.pyplot as plt

def fig_ctr(fout_name: str, ctrs: np.array, bins=100):
    """ 広告のCTRのヒストグラムを作図する。
    """

    plt.figure()
    plt.hist(ctrs, bins=bins)
    plt.savefig(fout_name)

def fig_rewards(fout_name: str, rewards: np.array, t_max: int, points_in_bin=10):
    """ 報酬の推移を作図する。
    """

    plt.figure() 
    x = np.array([x + 1 for x in range(t_max)])
    for algo_type, rewards_ in rewards.items():
        plt.plot(x[::points_in_bin], rewards_[::points_in_bin], label=algo_type)

    plt.legend()
    plt.savefig(fout_name)

def fig_cum_rewards(fout_name: str, cum_rewards: np.array):
    """ 累積報酬の棒グラフを作図する。
    """

    plt.figure()
    categories = list(cum_rewards.keys())
    ave = np.zeros(len(categories))
    stdev = np.zeros(len(categories))
    for i_cat, category in enumerate(categories):
        ave[i_cat] = np.mean(cum_rewards[category])
        stdev[i_cat] = np.std(cum_rewards[category])

    plt.bar(np.array(range(len(categories))), ave, tick_label=categories, yerr=stdev, align="center", capsize=10)
    plt.ylabel("average cumulative rewards")
    plt.savefig(fout_name)


if __name__ == '__main__':

    # 保存したデータの読み込み
    with open('results/result.pickle', 'rb') as fin:
        result = pickle.load(fin)
    
    ctrs = result['ctrs']
    t_max = result['t_max']
    ave_max = result['ave_max']
    rewards = result['rewards']
    cum_rewards = result['cum_rewards']

    # 広告CTRのヒストグラム
    fig_ctr('figs/ctr_hist.png', ctrs, bins=100)

    # 報酬の推移図
    fig_rewards('figs/rewards.png', rewards, t_max, points_in_bin=20)

    # 累積報酬
    fig_cum_rewards('figs/cum_rewards', cum_rewards)