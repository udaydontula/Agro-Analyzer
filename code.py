 
import pandas as pd

import cufflinks as Cf

Cf.set_config_file(offline=True, world_readable=True, theme='space')
import numpy as np
import matplotlib as mp
data = pd.read_csv("/home/Downloads/dataset2016.csv", encoding='latin-1')

data = data.drop(columns=['Unnamed: 0'])
data 
data['Profit'] = data['MSP']-data['Cost of Production']

data['Profit %'] = (data['Profit']/data['Cost of Production'])*100

data['Loan wavier'] = data['Profit %'] < 10
data
