"""loc and iloc (2)
loc and iloc also allow you to select both rows and columns from a DataFrame. To experiment, try out the following 
commands in the IPython Shell. Again, paired commands produce the same result.

cars.loc['IN', 'cars_per_cap']
cars.iloc[3, 0]

cars.loc[['IN', 'RU'], 'cars_per_cap']
cars.iloc[[3, 4], 0]

cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
cars.iloc[[3, 4], [0, 1]]"""

"""Instructions
* Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
* Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right.
"""

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
mor_drives_right = cars.loc['MOR', 'drives_right']
print(mor_drives_right)

# Print sub-DataFrame
russia_morocco_df = cars.loc[['RU', 'MOR'], ['country', 'drives_right']]
print(russia_morocco_df)
