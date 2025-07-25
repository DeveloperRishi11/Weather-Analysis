import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulate temperature data for 7 days
np.random.seed(42)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = np.random.normal(loc=30, scale=5, size=7)  # Mean 30°C, std dev 5°C

# Create a DataFrame
df = pd.DataFrame({
    'Day': days,
    'Temperature (°C)': np.round(temperature, 2)
})

print("📊 Weekly Temperature Data:\n", df)

# Plotting
plt.figure(figsize=(8, 4))
plt.plot(df['Day'], df['Temperature (°C)'], marker='o', linestyle='-', color='tomato')
plt.title('🌡️ Weekly Temperature Trends')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()