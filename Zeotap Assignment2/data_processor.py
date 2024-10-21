from collections import defaultdict
import time

ALERT_THRESHOLD = 35

def daily_summary(data):
    summary = defaultdict(list)

    for entry in data:
        day = time.strftime('%Y-%m-%d', time.gmtime(entry['time']))
        summary[day].append(entry['temp_celsius'])

    for day, temps in summary.items():
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        print(f"Date: {day}, Avg Temp: {avg_temp}, Max Temp: {max_temp}, Min Temp: {min_temp}")

def check_alerts(weather_data):
    if weather_data['temp_celsius'] > ALERT_THRESHOLD:
        print(f"Alert: {weather_data['temp_celsius']}°C exceeds threshold in {weather_data['city']}!")
