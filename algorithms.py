import random
import math
import numpy as np
from model import Advertisement

def random_sampling(adv_list: list, t_max: int) -> np.array:
    """ ランダムサンプリングを実行し、各時刻の報酬の配列を返す。
    """

    rewards = np.zeros(t_max)
    for i_t in range(t_max):

        # 表示する広告をランダムに選択する
        adv = random.choice(adv_list)

        # 広告の表示
        adv.show()

        # クリック判定
        if adv.is_clicked() is True:
            rewards[i_t] += 1.0
        else:
            pass
    
    return rewards

def egreedy(adv_list: list, t_max: int, epsilon: float) -> np.array:
    """ e-greedy法を実行し、各時刻の報酬の配列を変えす。 
    """

    # 1広告あたりのサンプリング時間の計算
    t_adv = math.floor(t_max * epsilon / len(adv_list))
    
    # 探索的サンプリング
    rewards = np.zeros(t_max)
    for i_t in range(t_adv * len(adv_list)):
            
        # 広告の選択
        adv = adv_list[i_t // t_adv]
        adv.show()

        # クリック判定
        if adv.is_clicked() is True:
            rewards[i_t] += 1.0
        else:
            pass

    # 報酬が最大の広告を選択
    rewards_sum = np.sum(rewards[0:t_adv * len(adv_list)]
                    .reshape(len(adv_list), t_adv), axis=1)
    adv = adv_list[np.argmax(rewards_sum)]

    # 報酬が最大の広告からサンプリング
    for i_t in range(t_adv * len(adv_list), t_max):

        # 広告の表示
        adv.show()

        # クリック判定
        if adv.is_clicked() is True:
            rewards[i_t] += 1.0
        else:
            pass
    
    return rewards

def ucb_policy(adv_list: list, t_max: int) -> np.array:
    """ UCB方策によるサンプリングを実行し、各時刻の報酬の配列を返す。
    """

    # 各広告を１回ずつ選択する
    rewards = np.zeros(t_max)
    for i_t in range(len(adv_list)):
        
        # 広告の選択
        adv = adv_list[i_t]
        adv.show()

        # クリック判定
        if adv.is_clicked() is True:
            rewards[i_t] += 1.0
        else:
            pass

    # UCBスコアに従ってサンプリング
    for i_t in range(len(adv_list), t_max):
        
        # UCBスコアの計算
        ucbs = np.array([ucb_score(adv, i_t) for adv in adv_list])

        # UCBスコア最大の広告を選択
        adv = adv_list[ucbs.argmax()]
        adv.show()

    # クリック判定
        if adv.is_clicked() is True:
            rewards[i_t] += 1.0
        else:
            pass
    
    return rewards


def thompson_sampling(adv_list: list, t_max: int, alpha=1.0, beta=1.0) -> np.array:
    """ トンプソンサンプリングを実行し、各時刻の報酬の配列を返す。
    """

    rewards = np.zeros(t_max)
    for i_t in range(t_max):

        # ベータ分布から期待値をサンプリング
        evs = np.array([np.random.beta(alpha + adv.total_clicked, 
                   beta + adv.total_showed - adv.total_clicked)
                   for adv in adv_list])
        
        # 広告の選択
        adv = adv_list[evs.argmax()]
        adv.show()

        # クリック判定
        if adv.is_clicked() is True:
            rewards[i_t] += 1.0
        else:
            pass

    return rewards

def ucb_score(adv: Advertisement, i_t: int) -> float:
    """ UCBスコアを計算して返す。
    """

    return adv.total_clicked / adv.total_showed + math.sqrt(math.log(i_t + 1) / 2 / adv.total_showed)