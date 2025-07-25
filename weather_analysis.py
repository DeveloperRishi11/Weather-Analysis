import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Seed for reproducibility
np.random.seed(42)

# Simulate temperature data for 7 days
np.random.seed(42)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = np.random.normal(loc=30, scale=5, size=7)  # Mean 30°C, std dev 5°C
temperature = np.round(temperature, 2)
humidity = np.random.randint(40, 90, size=7)
wind_speed = np.round(np.random.uniform(5, 15, size=7), 2)

# Create a DataFrame
df = pd.DataFrame({
    'Day': days,
    'Temperature (°C)': np.round(temperature, 2),
    'Humidity (%)': humidity,
    'Wind Speed (km/h)': wind_speed
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

# Humidity bar chart
plt.bar(df['Day'], df['Humidity (%)'], color='skyblue', alpha=0.6, label='Humidity (%)')

# Wind speed dashed line
plt.plot(df['Day'], df['Wind Speed (km/h)'], marker='x', linestyle='--', color='gray', label='Wind Speed (km/h)')

plt.title('📈 Weather Trends Over the Week')
plt.xlabel('Day')
plt.ylabel('Measurement')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()

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
fig, ax = plt.subplots(figsize=(8, 4))
line, = ax.plot([], [], marker='o', color='tomato')
ax.set_xlim(0, len(days)-1)
ax.set_ylim(np.min(temperature)-5, np.max(temperature)+5)
ax.set_xticks(range(len(days)))
ax.set_xticklabels(days)
ax.set_ylabel('Temperature (°C)')
ax.set_title('🌡️ Temperature Animation')

def update(frame):
    x = list(range(frame + 1))
    y = temperature[:frame + 1]
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=len(days), blit=True, interval=500)
plt.tight_layout()
plt.show()






