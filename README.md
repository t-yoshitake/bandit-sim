# bandit-sim
## 概要
バンディット問題の基本的な方策アルゴリズムのシミュレーションプログラム
https://qiita.com/tyoshitake/items/2ed890c56945c43774f5

## 構成
- simulation.py : シミュレーションを実行するメインプログラム
- model.py : シミュレーション対象の広告モデル
- algorithms.py : 各種方策アルゴリズムのプログラム
- draw.py : 作図用プログラム  

## 実行環境
- python 3.6.5
- numpy 1.16.4
- matplotlib 3.1.0

## 実行方法
### シミュレーションの実行
```
python simulation.py
```
実行後resultsディレクトリ内に結果をまとめたpickleファイルが作成されます。

### 作図の実行
```
python draw.py
```
resultsディレクトリ内の結果ファイル(.pickle)を読み込み、作図を実行します。画像ファイルはfigsディレクトリ内に作成されます。
作成されるのは以下の図です。
- 広告のCTRの分布図
- 報酬の推移図
- 累積報酬の比較図
  
# 参考
qiita記事
https://qiita.com/tyoshitake/items/2ed890c56945c43774f5
