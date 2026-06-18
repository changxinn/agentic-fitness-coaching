from tools.storage import load_data, save_data, today_str


def log_workout(description: str) -> str:
    """
    Log a completed or planned workout entry.
    Format: free text, e.g. '30 min run, easy pace' or 'legs: squats 3x10'.
    """
    data = load_data()
    entry = {
        "date": today_str(),
        "description": description.strip(),
    }
    data["workouts"].append(entry)
    save_data(data)
    return f"Workout logged for {entry['date']}: {description.strip()}"


def exercise_lookup(exercise_name: str) -> str:
    """
    Return basic guidance for a named exercise.
    """
    exercises = {
        "squat": "Bodyweight or barbell squat: keep chest up, knees track over toes, depth to parallel or below.",
        "push-up": "Push-up: straight line head to heels, lower chest near floor, full lockout at top.",
        "deadlift": "Deadlift: hinge at hips, neutral spine, bar close to shins, drive through floor.",
        "rdl": "Romanian deadlift (RDL): soft knee bend, hinge hips back, bar stays close to legs, feel hamstring stretch.",
        "plank": "Plank: elbows under shoulders, brace core, avoid sagging hips.",
        "run": "Easy run: conversational pace; increase weekly mileage by no more than ~10%.",
        "bench press": "Bench press: retract scapula, feet planted, controlled bar path to mid-chest.",
        "row": "Row (barbell/dumbbell): hinge slightly, pull to lower ribs, squeeze shoulder blades.",
        "lunge": "Lunge: step long, front knee over ankle, torso upright, alternate legs.",
    }

    key = exercise_name.strip().lower()
    for name, tip in exercises.items():
        if name in key or key in name:
            return f"{name.title()} — {tip}"

    return (
        f"No detailed entry for '{exercise_name}'. "
        "General tip: start light, focus on form, and progress gradually."
    )
