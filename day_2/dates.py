from datetime import datetime
from datetime import timedelta, date

# Get the current time
now = datetime.now()
print(f"Current datetime: {now}")

# Get the current utc time
utc = datetime.utcnow()
print(f"Current UTC datetime: {utc}")

# Get today's date
today = date.today()
print(f"Today's date: {today}")

# Add 2 days, 2hr, 5mins, 3sec to current day
future = now + timedelta(days=2, hours=2, minutes=5, seconds=3)
print(f"Future date: {future}") 


# Date formatting

now = datetime.now()
formatted = now.strftime("%d-%m-%Y")
print(f"Formatted date: {formatted}")

iso_date = now.isoformat()
print(f"ISO date: {iso_date}")
print()

# Get current datetime in utc with timezone
from datetime import timezone
dt = datetime.now(timezone.utc)
print("UTC datetime with timezone: ", dt)

