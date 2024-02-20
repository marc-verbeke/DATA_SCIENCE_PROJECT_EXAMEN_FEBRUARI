import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("../data/geboortes.xlsx")
df_counts = df.groupby('dag').size()
gemiddelde = df_counts.mean()
bovengrens = gemiddelde * 1.5
ondergrens = gemiddelde * 0.5 + 130

outliers = df_counts[(df_counts > bovengrens) | (df_counts<ondergrens)]

print('de outliers zijn: ')
print(outliers)

ex_boven_df = df[(df['dag'] != 1)]
ex_outliers_df = ex_boven_df[(ex_boven_df['dag'] != 182)]
