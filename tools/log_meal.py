from tools.storage import load_data, save_data, today_str


def log_meal(description: str) -> str:
    """
    Log a meal or snack.
    Format: free text, e.g. 'breakfast: oats, banana, coffee'.
    """
    data = load_data()
    entry = {
        "date": today_str(),
        "description": description.strip(),
    }
    data["meals"].append(entry)
    save_data(data)
    return f"Meal logged for {entry['date']}: {description.strip()}"
