import numpy as np

# Create random temperature readings for 30 days, 7 readings per day
# Values between 15 and 35 degrees
temperature_readings = np.random.randint(15, 35, (30, 7))

# 1. Get temperatures for the 15th day (index 14)
day_15_temps = temperature_readings[14]
print("Temperatures for 15th day:", day_15_temps)

# 2. Calculate average temperature for each day
daily_averages = np.mean(temperature_readings, axis=1)
print("\nDaily average temperatures:", daily_averages)

# 3. Calculate average temperature for the entire month
monthly_average = np.mean(temperature_readings)
print("\nMonthly average temperature:", monthly_average)

# 4. Get all temperatures above 30 degrees
high_temps = temperature_readings[temperature_readings > 30]
print("\nTemperatures above 30 degrees:", high_temps)

# 5. Calculate weekly average temperatures (assuming 4 weeks)
weekly_averages = np.array([np.mean(temperature_readings[i:i+7]) for i in range(0, 28, 7)])
print("\nWeekly average temperatures:", weekly_averages)

# 6. Get temperatures for the first week
first_week = temperature_readings[:7]
print("\nFirst week temperatures:", first_week)

# 7. Increase temperatures below 20 degrees by 2 degrees
temperature_readings[temperature_readings < 20] += 2
print("\nAfter increasing low temperatures:")
print(temperature_readings)

# 8. Get temperatures for specific days (1st, 10th, and 20th)
specific_days = temperature_readings[[0, 9, 19]]
print("\nTemperatures for 1st, 10th, and 20th days:", specific_days)

# 9. Get the highest temperature for each day
daily_highs = np.max(temperature_readings, axis=1)
print("\nHighest temperature each day:", daily_highs)

# 10. Find the day with the highest average temperature
hottest_day_index = np.argmax(daily_averages)
print("\nDay with highest average temperature:", hottest_day_index + 1)
print("Highest average temperature:", daily_averages[hottest_day_index])