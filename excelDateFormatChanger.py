import pandas as pd
import os
os.chdir('insert your path here')
files = os.listdir(os.getcwd())

for file in files:
    df = pd.read_csv(file, names = ['meter','date','value'])

    frmt0 = '%Y-%m-%d %H:%M:%S.%f'
    frmt1 = '%m/%d/%Y %H:%M:%S'

    df['date'] = pd.to_datetime(df.date, format = frmt0)
    df['date'] = df['date'].dt.strftime(frmt1)

    df.to_csv('Edited_'+file, header=None, index = None)
