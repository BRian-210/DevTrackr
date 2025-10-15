from datetime import datetime
def parse_hours(value):
    try:
        return float(value)
    except Exception:
        raise ValueError('Invalid hours value. Provide a number, e.g., 1.5')
def human_dt(dt):
    if not dt:
        return ''
    return dt.strftime('%Y-%m-%d %H:%M:%S')
