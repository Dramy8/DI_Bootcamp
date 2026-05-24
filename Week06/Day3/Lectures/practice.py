#%%
# pip3 install numpy
# import numpy as np
# print(np.__version__)

import numpy as np

movie_ratings = np.array([
    [5, 4, 4, 1, 3],
    [1, 4, 3, 1, 2],
    [4, 2, 5, 5, 1]
])

average_ratings = np.mean(movie_ratings, axis=1)
viewer_preferences = np.argmax(movie_ratings, axis=0) + 1

print("Average ratings:", average_ratings)
print("Viewer preferences:", viewer_preferences)
# %%
import numpy as np

# Temperature data matrix: rows = cities, columns = days
temperature_data = np.array([
    [27, 20, 15, 18, 26, 18, 22],
    [24, 18, 20, 17, 19, 22, 21],
    [23, 23, 27, 25, 16, 21, 22],
    [22, 29, 23, 16, 20, 24, 28]
])

average_temperatures = np.mean(temperature_data, axis=1)
max_temperatures = np.max(temperature_data, axis=1)
min_temperatures = np.min(temperature_data, axis=1)

day_1 = temperature_data[:, 0]
day_7 = temperature_data[:, -1]
difference = day_7 - day_1

print("Average temperature for each city:", average_temperatures)
print("Maximum temperature for each city:", max_temperatures)
print("Minimum temperature for each city:", min_temperatures)
print("Day 1 temperatures:", day_1)
print("Day 7 temperatures:", day_7)
print("Difference Day 7 - Day 1:", difference)

# %%


# %%
!pip install pandas


# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Make random results reproducible
np.random.seed(42)

# 1. Create the time series dataset
dates = pd.date_range(start="2022-01-01", end="2022-12-31", freq="D")

temperature = np.random.uniform(10, 35, size=len(dates))
humidity = np.random.uniform(30, 90, size=len(dates))

df = pd.DataFrame({
    "Date": dates,
    "Temperature": temperature,
    "Humidity": humidity
})

# 2. Basic analysis
print("First rows:")
print(df.head())

print("\nTemperature statistics:")
print("Mean:", df["Temperature"].mean())
print("Median:", df["Temperature"].median())
print("Standard deviation:", df["Temperature"].std())

print("\nHumidity statistics:")
print("Mean:", df["Humidity"].mean())
print("Median:", df["Humidity"].median())
print("Standard deviation:", df["Humidity"].std())

highest_temperature_index = df["Temperature"].idxmax()
highest_humidity_index = df["Humidity"].idxmax()

print("\nHighest temperature date:")
print(df.loc[highest_temperature_index, "Date"])

print("\nHighest humidity date:")
print(df.loc[highest_humidity_index, "Date"])

# 3. Rolling window / moving average
df["Temperature_7day_avg"] = df["Temperature"].rolling(window=7).mean()
df["Humidity_7day_avg"] = df["Humidity"].rolling(window=7).mean()

print("\nFirst 10 rows with rolling averages:")
print(df.head(10))

# 4. Bonus plots
plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Temperature"], label="Temperature", alpha=0.7)
plt.plot(df["Date"], df["Humidity"], label="Humidity", alpha=0.7)
plt.title("Temperature and Humidity Over 2022")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.show()

plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Temperature"], label="Original Temperature", alpha=0.3)
plt.plot(df["Date"], df["Temperature_7day_avg"], label="7-day Temperature Average", linewidth=2)

plt.plot(df["Date"], df["Humidity"], label="Original Humidity", alpha=0.3)
plt.plot(df["Date"], df["Humidity_7day_avg"], label="7-day Humidity Average", linewidth=2)

plt.title("Original Data vs 7-day Moving Average")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.show()
# %%
# import sys
# !{sys.executable} -m pip install pandas

# %%
