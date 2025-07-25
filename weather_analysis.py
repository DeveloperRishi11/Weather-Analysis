import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulate temperature data for 7 days
np.random.seed(42)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = np.random.normal(loc=30, scale=5, size=7)  # Mean 30°C, std dev 5°C
temperature = np.round(temperature, 2)

# Create a DataFrame
df = pd.DataFrame({
    'Day': days,
    'Temperature (°C)': np.round(temperature, 2)
})

print("📊 Weekly Temperature Data:\n", df)

# Calculate stats
avg_temp = np.mean(temperature)
min_temp = np.min(temperature)
max_temp = np.max(temperature)
min_day = df.loc[df['Temperature (°C)'] == min_temp, 'Day'].values[0]
max_day = df.loc[df['Temperature (°C)'] == max_temp, 'Day'].values[0]

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(df['Day'], df['Temperature (°C)'], marker='o', linestyle='-', color='tomato', label='Temp')
plt.axhline(avg_temp, color='blue', linestyle='--', label=f'Average: {avg_temp:.2f}°C')

# Annotate max and min
plt.scatter(max_day, max_temp, color='green', s=100, zorder=5, label=f'Max: {max_temp:.2f}°C')
plt.scatter(min_day, min_temp, color='purple', s=100, zorder=5, label=f'Min: {min_temp:.2f}°C')



# Beautify
plt.title('🌡️ Weekly Temperature Trends', fontsize=14)
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('weekly_temperature_chart.png')  # Save the plot
plt.show()




