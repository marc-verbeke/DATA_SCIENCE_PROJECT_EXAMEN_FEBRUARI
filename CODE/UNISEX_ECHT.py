import pandas as pd

df = pd.read_excel("../data/geboortes.xlsx")

df_unisex = df.groupby(['naam'])[['man', 'vrouw']].sum().reset_index()
totaal_man = df_unisex['man'].sum()
totaal_vrouw = df_unisex['vrouw'].sum()
df_unisex['man & vrouw'] = df_unisex['man'] + df_unisex['vrouw']
df_unisex['unisex'] = (df_unisex['man'] != 0) & (df_unisex['vrouw'] != 0)
df_unisex_filtered = df_unisex[df_unisex['unisex']]
df_echt_unisex = df_unisex_filtered.copy()

df_echt_unisex['echt_unisex'] = (df_echt_unisex['man'] <= 1.5 * df_echt_unisex['vrouw']) & (df_echt_unisex['vrouw'] <= 1.5 * df_unisex_filtered['man'])
df_echt_unisex_filtered = df_echt_unisex[df_echt_unisex['echt_unisex']]

print(f"Er zijn {df_echt_unisex_filtered['unisex'].count()} elementen in de 'unisex' kolom.")

df_man = df_echt_unisex_filtered.copy()
df_man.sort_values(by='man', ascending=False, inplace=True)
print(f"De meest populaire echte unisex naam bij mannen is: {df_man.iloc[0,0]} ({df_man.iloc[0,1]})")

df_vrouw = df_echt_unisex_filtered.copy()
df_vrouw.sort_values(by='vrouw', ascending=False, inplace=True)

print(f"De meest populaire echte unisex naam bij vrouwen is: {df_vrouw.iloc[0,0]} ({df_vrouw.iloc[0,2]})")

df_manvrouw = df_echt_unisex_filtered.copy()
df_manvrouw.sort_values(by='man & vrouw', ascending=False, inplace=True)

print(f"De meest populaire echte unisex naam is: {df_manvrouw.iloc[0,0]} ({df_manvrouw.iloc[0,3]})")

print(f"{round(df_man['man'].sum()/totaal_man*100,1)}% van de mannen hebben een echte unisex naam")
print(f"{round(df_vrouw['vrouw'].sum()/totaal_vrouw*100,1)}% van de vrouwen hebben een echte unisex naam")