import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("../data/geboortes.xlsx")
df_counts = df.groupby('dag').size()

print(df_counts)

df_counts.plot(kind='line', figsize=(10, 6))
plt.xlabel('Geboortedatum')
plt.ylabel('Aantal keer voorgekomen')
plt.title('Lijndiagram van Geboortedata')
plt.grid(True)
plt.show()