import os
import pandas as pd

path = '../DATA/geboortes'
df = pd.DataFrame()

for filename in os.listdir(path):
    if filename.endswith('.csv'):
        datum = pd.to_datetime(filename.split('.')[0])
        filepath = os.path.join(path, filename)
        temp_df = pd.read_csv(filepath)
        temp_df['geboortedatum'] = datum
        temp_df['dag']=datum.dayofyear
        temp_df.loc[temp_df['geslacht'].str.lower() == 'mannelijk', 'man'] = 1
        temp_df.loc[temp_df['geslacht'].str.lower() == 'vrouwelijk', 'vrouw'] = 1


        df = pd.concat([df, temp_df], ignore_index=True)

output_path = os.path.join('../DATA', 'geboortes.xlsx')
df.to_excel(output_path, index=False)

print(f'==============================================================')
print(f'DATAFRAME IS BEWAARD: {output_path}')
print(f'==============================================================')
print(df.head())
print(f'==============================================================')
