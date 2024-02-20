import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("../data/geboortes.xlsx")

df_unisex = df.groupby(['naam'])[['man', 'vrouw']].sum().reset_index()
df_unisex['man & vrouw'] = df_unisex['man'] + df_unisex['vrouw']
df_unisex['unisex'] = (df_unisex['man'] != 0) & (df_unisex['vrouw'] != 0)
df_unisex_filtered = df_unisex[df_unisex['unisex']]
df_echt_unisex = df_unisex_filtered.copy()

df_echt_unisex['echt_unisex'] = (df_echt_unisex['man'] <= 1.5 * df_echt_unisex['vrouw']) & (df_echt_unisex['vrouw'] <= 1.5 * df_unisex_filtered['man'])
df_echt_unisex_filtered = df_echt_unisex[df_echt_unisex['echt_unisex']]

df_echt_unisex_filtered['percentage_man'] = (df_echt_unisex_filtered['man'] / df_echt_unisex_filtered['man & vrouw']) * 100
df_echt_unisex_filtered['percentage_vrouw'] = (df_echt_unisex_filtered['vrouw'] / df_echt_unisex_filtered['man & vrouw']) * 100

print(df_echt_unisex_filtered)

sns.set(style='white')
df_echt_unisex_filtered.set_index('naam')[['percentage_man', 'percentage_vrouw']].plot(kind='barh', stacked=True, color=['steelblue', 'red'])
plt.show()

