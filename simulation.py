import random
import math
import pickle
import numpy as np
from model import Advertisement
from algorithms import random_sampling, egreedy, ucb_policy, thompson_sampling

def ctr_exp(n: int, ave: float) -> np.array:
    """ 指数分布から広告のctrをサンプリングし配列として返す。
    """

    return np.random.exponential(scale=ave, size=n)

if __name__ == '__main__':

    np.random.seed(1)
    random.seed(1)

    # 広告ctrの生成
    ctrs = ctr_exp(n=50, ave=0.08)

    # シミュレーション条件
    t_max = 10000 # 最大時間
    ave_max = 5000 # サンプリングの繰り返し数

    # 報酬
    rewards = {
        "random"      : np.zeros(t_max),
        "egreedy-0.3" : np.zeros(t_max),
        "egreedy-0.6" : np.zeros(t_max),
        "ucb"         : np.zeros(t_max),
        "thompson"    : np.zeros(t_max),
    }

    # 累積報酬
    cum_rewards = {
        "random"      : np.zeros(ave_max),
        "egreedy-0.3" : np.zeros(ave_max),
        "egreedy-0.6" : np.zeros(ave_max),
        "ucb"         : np.zeros(ave_max),
        "thompson"    : np.zeros(ave_max),
    }

    # アルゴリズム関数
    def egreedy_03(adv_list: list, t_max: int) -> np.array:
        return egreedy(adv_list, t_max, epsilon=0.3)

    def egreedy_06(adv_list: list, t_max: int) -> np.array:
        return egreedy(adv_list, t_max, epsilon=0.6)

    algorithm = {
        "random"      : random_sampling,
        "egreedy-0.3" : egreedy_03,
        "egreedy-0.6" : egreedy_06,
        "ucb"         : ucb_policy,
        "thompson"    : thompson_sampling,
    }

    # シミュレーション実行
    for algo_type in algorithm.keys():

        rewards_ = rewards[algo_type]
        cum_rewards_ = cum_rewards[algo_type]
        algorithm_ = algorithm[algo_type]

        for i_ave in range(ave_max):
            
            # 広告インスタンスの生成
            adv_list = [Advertisement(ctr) for ctr in ctrs]

            # アルゴリズムの実行
            rewards_out = algorithm_(adv_list, t_max)

            rewards_ += rewards_out

            # 累積報酬の計算
            cum_rewards_[i_ave] = np.sum(rewards_out)
        
        rewards_ /= ave_max

        # 結果の出力
        print(' *' + algo_type)
        print('  * ave(total): %f' % (np.mean(cum_rewards_)))
        print('  * std(total): %f' % (np.std(cum_rewards_)))

    # 結果の保存
    result = {
        'ctrs': ctrs,
        't_max': t_max,
        'ave_max': ave_max,
        'rewards': rewards,
        'cum_rewards': cum_rewards,
    }

    with open('results/result.pickle', 'wb') as fout:
        pickle.dump(result, fout)