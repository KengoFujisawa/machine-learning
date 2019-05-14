import math
import numpy as np
import pandas as pd
#2019年4月20日から20日のデータを発生
dates=pd.date_range("2019/04/20",periods=20)
#0から100までの20*2の乱数
nums=np.random.randint(0,100, (20,2))
column=["既存","新規"]
#データをnums, 縦方向のラベル(index)をdates, 横方向のラベル(columns)をcolumnとしたデータフレームを作成
df=pd.DataFrame(nums,index=dates,columns=column)
column2=["誤差"]
#標準正規分布から20*1の乱数
nums2=np.random.normal(0,1,size=(20,1))
df2=pd.DataFrame(nums2,index=dates,columns=column2)
#日付をキーにデータフレームの結合
mergedata=pd.merge(df,df2,on=dates)
#列の抽出
col_df=df["新規"]
#条件で抽出
col_cond=df[df["新規"]<50]
print(col_cond)
#特定の行の抽出

#1行目から5行目まで抽出
row_df=df[0:5]
#20190426から20190501の行を抽出
row_df2=df["20190426":"20190501"]
#新規でソート
sort_df=df.sort_values(by="新規")
#降順でソート
sort_df=df.sort_values(by="新規",ascending=False)
#行数
num_of_row=len(df)
#要素数
element=df.size
#基本統計量について
df_mean=df.mean()
df_std=df.std()
df_max=df.max()
df_min=df.min()
df_var=df.var()
