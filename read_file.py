import pandas as pd


data=pd.read_csv('nyc_weather.csv')
ls={'Temperature':0, 'Events': 'No Event'}
data.fillna(ls, inplace=True)
print(data)
g=data.groupby('Temperature')
#print(g.get_group(40))
tabel={"Name": ["amir", "ali", "hasan"],
       "Age": [55, 66, 33]
       }
# df=pd.DataFrame(tabel)
# with pd.ExcelWriter('amirExel.xlsx') as write:
#    df.to_excel(write, sheet_name="first")
#    data.to_excel(write, sheet_name="second")
# print(data.iloc[:,0:5])
# ind=data.columns.get_loc("Humidity")
# data.set_index('EST', inplace=True)
# print(data.loc['1/1/2016'])
# data.reset_index(inplace=True)