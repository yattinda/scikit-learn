%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

#-10から10までを100ステップに分けた列を配列として生成
x = np.linspace(-10, 10, 100)
#sin関数を用いて2つめの配列を生成
y = np.sin(x)
#plot関数は一方の配列に対して他方の配列をプロットする
plt.plot(x, y, marker="x")

#jupyternotebookで実行
