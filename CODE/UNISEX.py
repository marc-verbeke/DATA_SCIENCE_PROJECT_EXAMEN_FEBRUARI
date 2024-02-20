import pandas as pd

df = pd.read_excel("../data/geboortes.xlsx")

df_unisex = df.groupby(['naam'])[['man', 'vrouw']].sum().reset_index()
df_unisex['man & vrouw'] = df_unisex['man'] + df_unisex['vrouw']
df_unisex['unisex'] = (df_unisex['man'] != 0) & (df_unisex['vrouw'] != 0)
df_unisex_filtered = df_unisex[df_unisex['unisex']]

print(f"Er zijn {df_unisex_filtered['unisex'].count()} elementen in de 'unisex' kolom.")

df_man = df_unisex_filtered.copy()
df_man.sort_values(by='man', ascending=False, inplace=True)

print(f"De meest populaire unisex naam bij mannen is: {df_man.iloc[0,0]} ({df_man.iloc[0,1]})")

df_vrouw = df_unisex_filtered.copy()
df_vrouw.sort_values(by='vrouw', ascending=False, inplace=True)

print(f"De meest populaire unisex naam bij vrouwen is: {df_vrouw.iloc[0,0]} ({df_vrouw.iloc[0,2]})")

df_manvrouw = df_unisex_filtered.copy()
df_manvrouw.sort_values(by='man & vrouw', ascending=False, inplace=True)

print(f"De meest populaire unisex naam is: {df_manvrouw.iloc[0,0]} ({df_manvrouw.iloc[0,3]})")
