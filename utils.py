from datetime import datetime, timedelta

def time_ago(date):
    """Calculates the time difference in a human-readable format."""
    now = datetime.now()
    diff = now - date

    # Calculate the different components of the time difference
    seconds = diff.total_seconds()
    minutes = seconds // 60
    hours = minutes // 60
    days = diff.days
    weeks = days // 7
    months = days // 30
    years = days // 365

    # Determine the appropriate human-readable format based on the time difference
    if seconds < 60:
        return f"{int(seconds)} seconds ago"
    elif minutes < 60:
        return f"{int(minutes)} minutes ago"
    elif hours < 24:
        return f"{int(hours)} hours ago"
    elif days < 7:
        return f"{days} days ago"
    elif weeks < 4:
        return f"{weeks} weeks ago"
    elif months < 12:
        return f"{months} months ago"
    else:
        return f"{years} years ago"
    
    