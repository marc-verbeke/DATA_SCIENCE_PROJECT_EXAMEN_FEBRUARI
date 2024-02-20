import pandas as pd

datum = '2019-9-30'

datum2 = pd.to_datetime(datum, format='%Y-%m-%d')
print(datum2)

day_of_year = datum2.dayofyear
print(f"The day of the year for {datum} is {day_of_year}.")