

import pandas as pd 
import matplotlib.pyplot as plt

"""
# 使用Series繪製折線圖

population=[860,1100,1450,1800,2020,2200,2260]
tw=pd.Series(population,index=range(1950,2011,10))
tw.plot(title='Population in Taiwan')
plt.xlabel("YEAR")
plt.ylabel("Population")
plt.show()

"""


"""
# DataFrame繪製折線圖

cities={'population':[1000,850,800,1500,600,800],'town':['new york','chicago','bangkok','tokyo','singapore','hongkong']}

tw=pd.DataFrame(cities,columns=['population'],index=cities['town'])

# print(tw)

tw.plot(title='Population in the world')
plt.xlabel('City')
plt.ylabel('Population')
plt.show()

"""
"""
# 直條圖設計

population=[860,1100,1450,1800,2020,2200,2260]
tw=pd.Series(population,index=range(1950,2011,10))

tw.plot(title='Population in the world',kind='bar')

plt.show()

"""
"""

# 一張圖表含不同數值資料
cities={'population':[1000,850,800,1500,600,800],
        'area':[400,500,850,300,200,320],
        'town':['new york','chicago','bangkok','tokyo','singapore','hongkong']}

tw=pd.DataFrame(cities,columns=['population','area'],index=cities['town'])

tw.plot(title='Population in the world')
plt.xlabel('city')
plt.show()

"""
"""
# 多個數值軸的設計
# 需要使用subplots()，可以在一個圖表內顯示多組不同軸的數據
# fig,ax=subplots() fig是整個圖表物件，ax是第一個軸
# ax2=ax.twinx() 建立第二個軸物件 ax2

cities={'population':[1000,850,800,1500,600,800],
        'area':[400,500,850,300,200,320],
        'town':['new york','chicago','bangkok','tokyo','singapore','hongkong']}

tw=pd.DataFrame(cities,columns=['population','area'],index=cities['town'])

fig, ax=plt.subplots()
fig.suptitle("City Statistics")
ax.set_ylabel("Population")
ax.set_xlabel("City")

ax2=ax.twinx()
ax2.set_ylabel("Area")
tw['population'].plot(ax=ax,rot=90) #繪製人口數線
tw['area'].plot(ax=ax2,style='g-')  #繪製面積線

ax.legend(loc=1)   #圖例位置在右上
ax2.legend(loc=2)  #圖例位置在左上
plt.show()

"""

# 使用Series物件設計圓餅圖
# 使用plot.pie()

# labels:圓餅圖項目所組成的串列
# colors:圓餅圖顏色所組成的串列，如過省略則用預設顏色
# explode:可設定是否從圓餅圖分離的串列，0表示不分離，一般可以用0.1分離
# autopct:表示項目的百分比格式，基本語法是"%" 例如"%2.2%%"表示整數兩位數，小數兩位數

fruits=['Apples','Bananas','Grapes','Pears','Oranges']
s =pd.Series([2300,5000,1200,2500,2900],index=fruits,name='Fruits Shop')
explode=[0.4,0,0,0.2,0]
s.plot.pie(autopct='%1.1%%')
plt.show()
