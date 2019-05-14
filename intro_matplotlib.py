import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
column=["Y","X1","X2"]
num=np.random.normal(20,2,size=50)
num2=np.random.normal(10,1,size=50)
num3=np.random.normal(10,1,size=50)
#2つ以上の1次元リストを2次元リストに変換
data=[list(e) for e in zip(num,num2,num3)]
#データフレームの生成
df=pd.DataFrame(data,columns=column)
#numとnum2の散布図
#plt.plot(num2,num, "o",label="my data")
#numのヒストグラム
#plt.hist(num,bins=5)
#numをソート
num_sort=sorted(num)
#折れ線グラフ
#plt.plot(num,"o-")
left=range(1,13)
height=np.random.randint(10,100,size=12)
#横軸left縦軸heightの棒グラフ
#plt.bar(left,height,width=0.5,color="#aaaa00",edgecolor="#000000",linewidth=1.2)
#plt.show()
