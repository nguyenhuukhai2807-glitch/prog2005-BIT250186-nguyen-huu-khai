import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
cities = pd.read_csv('california_cities.csv')

# Calculate population density (people per square kilometer)
cities['density'] = cities['population_total'] / cities['area_total_km2']
# Select the top 15 cities with the highest population density
top_density = cities.sort_values(by='density', ascending=False).head(15)
# Plot horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(top_density['city'], top_density['density'], color='coral')
plt.xlabel('Population Density (people/km2)')
plt.title('Top 15 Most Densely Populated Cities in California')
plt.gca().invert_yaxis() # Highest density at the top
plt.tight_layout()
plt.show()


