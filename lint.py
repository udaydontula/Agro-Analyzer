import pandas as pd
import cufflinks as Cf
Cf.set_config_file(offline = True, world_readable = True, theme = 'space')
data = pd.read_csv("/home/Downloads/data encoding = 'latin-1')
data = data.drop(columns = ['Unnamed :0']
data['Profit'] = data['MSP']-data['Cost of production']
data['Profit %']=(data['Profit']/data['Cost of Production'])*100
data['Loan wavier']=data['Profit %']<10
data.to_csv('final file 2019.csv')
data1=data.drop(columns=['Mean'])
data1=data1.drop(columns=['Min'])


