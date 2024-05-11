from datetime import datetime, timedelta
def time_ago(date):
  now = datetime.utcnow()
  diff = now - date

  seconds = diff.seconds
  minutes = diff.seconds / 60
  hours = minutes / 60
  days = hours / 24
  weeks = days / 7

  # Check for seconds and minutes first
  if seconds < 60:
    return f"{int(seconds) } seconds ago"
  elif minutes < 60:
    return f"{ int(minutes)} minutes ago"
  # Then check for hours, days, and weeks
  elif hours < 24:
    return f"{int(hours)} hours ago"
  elif days < 7:
    return f"{int(days)} days ago"
  else:
    return f"{int(weeks)} weeks ago"

# Register the filter with your Flask app (usually in your app factory)
