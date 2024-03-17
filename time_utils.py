from datetime import datetime

def get_current_timestamp():
    return datetime.now().timestamp()

def format_timestamp(timestamp, format="%Y-%m-%d %H:%M:%S"):
    return datetime.fromtimestamp(timestamp).strftime(format)
