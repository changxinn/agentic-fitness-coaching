from tools.storage import load_data, save_data, today_str


def log_sleep(hours: str, quality: str = "fair") -> str:
    """
    Log sleep duration and quality.
    hours: e.g. '7.5' or '7 hours'
    quality: poor, fair, good, or excellent
    """
    data = load_data()
    entry = {
        "date": today_str(),
        "hours": hours.strip(),
        "quality": quality.strip().lower(),
    }
    data["sleep_logs"].append(entry)
    save_data(data)
    return (
        f"Sleep logged for {entry['date']}: {entry['hours']} hours, "
        f"quality: {entry['quality']}"
    )
