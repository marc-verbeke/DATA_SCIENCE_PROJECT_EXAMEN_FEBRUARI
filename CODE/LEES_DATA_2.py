import os
import pandas as pd

path = '../DATA/geboortes'
df = pd.DataFrame()

for filename in os.listdir(path):
    if filename.endswith('.csv'):
        datum = filename.split('.')[0]
        filepath = os.path.join(path, filename)
        temp_df = pd.read_csv(filepath)
        temp_df['geboortedatum'] = datum
        df = pd.concat([df, temp_df], ignore_index=True)

output_path = os.path.join('../DATA', 'geboortes2.xlsx')
df.to_excel(output_path, index=False)

print(f'==============================================================')
print(f'DATAFRAME IS BEWAARD: {output_path}')
print(f'==============================================================')
print(df.head())
print(f'==============================================================')
