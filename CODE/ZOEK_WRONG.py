import pandas as pd
import os

df = pd.read_excel("../data/geboortes2.xlsx")
df_wrong1 = df[df['geboortedatum'] == '2019-2-29'].reset_index()
df_wrong1['reden fout'] = '29/2/2019 bestaat niet'
df_wrong2 = df[df['geboortedatum'] == '2019-1-1'].reset_index()
df_wrong2['reden fout'] = '2019-01-01'
df_wrong3 = df[df['geboortedatum'] == '2019-7-1'].reset_index()
df_wrong3['reden fout'] = '2019-07-01'

print(df_wrong1)
print(df_wrong2)
print(df_wrong3)


df_wrong = df_wrong1
df_wrong = pd.concat([df_wrong, df_wrong2], ignore_index=True)
df_wrong = pd.concat([df_wrong, df_wrong3], ignore_index=True)


print(df_wrong)


output_path = os.path.join('../DATA', 'geboortes_met_fout_in_datum.xlsx')
df_wrong.to_excel(output_path, index=False)

print(f'==============================================================')
print(f'DATAFRAME IS BEWAARD: {output_path}')
print(f'==============================================================')
print(df_wrong.head())
print(f'==============================================================')