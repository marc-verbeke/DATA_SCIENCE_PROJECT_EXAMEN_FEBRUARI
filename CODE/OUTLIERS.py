import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("../data/geboortes.xlsx")
df_counts = df.groupby('dag').size()
gemiddelde = df_counts.mean()
bovengrens = gemiddelde * 1.5
ondergrens = gemiddelde * 0.5
print(f"het gemiddelde van de geboortes = {gemiddelde}")
print(f"de bovengrens 50% = {bovengrens}")
print(f"de ondergrens 50% = {ondergrens}")

outliers = df_counts[(df_counts > bovengrens) | (df_counts<ondergrens)]

print('de outliers zijn: ')
print(outliers)

ex_boven_df = df[(df['dag'] != 1)]
ex_outliers_df = ex_boven_df[(ex_boven_df['dag'] != 182)]

df_counts = ex_outliers_df.groupby('dag').size()

df_counts.plot(kind='line', figsize=(10, 6))
plt.xlabel('Geboortedatum')
plt.ylabel('Aantal keer voorgekomen')
plt.title('Lijndiagram van Geboortedata')
plt.grid(True)
plt.show()


