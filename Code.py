# Check-Battery-of-Laptop-with-Python

from pynotifier import Notification # pip install py-notifier
import psutil # pip install psutil

battery = psutil.sensors_battery()
percent = battery.percent

Notification("Battery Percentage", str(percent) + "%Percent Remaining", duration=10).send()
