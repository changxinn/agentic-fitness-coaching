import re


def _extract_measurements(text: str) -> tuple[float | None, float | None]:
    weight_kg = None
    height_m = None

    weight_match = re.search(
        r"(\d+(?:\.\d+)?)\s*(?:kg|kilograms?)\b",
        text,
        re.IGNORECASE,
    )
    if weight_match:
        weight_kg = float(weight_match.group(1))

    height_cm_match = re.search(
        r"(\d+(?:\.\d+)?)\s*(?:cm|centimeters?)\b",
        text,
        re.IGNORECASE,
    )
    if height_cm_match:
        height_m = float(height_cm_match.group(1)) / 100
    else:
        height_m_match = re.search(
            r"(\d+(?:\.\d+)?)\s*(?:m|meters?)\b",
            text,
            re.IGNORECASE,
        )
        if height_m_match:
            height_m = float(height_m_match.group(1))

    return weight_kg, height_m


def _bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "underweight"
    if bmi < 25:
        return "healthy weight"
    if bmi < 30:
        return "overweight"
    return "obesity range"


def get_bmi(measurements: str) -> str:
    """
    Calculate BMI from free text containing weight in kg and height in cm or m.
    Example: '70 kg, 175 cm' or 'weight 70kg height 1.75m'.
    """
    weight_kg, height_m = _extract_measurements(measurements)

    if weight_kg is None or height_m is None:
        return "Error: provide weight in kg and height in cm or m, e.g. get_bmi: 70 kg, 175 cm"

    if weight_kg <= 0 or height_m <= 0:
        return "Error: weight and height must be positive numbers."

    bmi = weight_kg / (height_m * height_m)
    category = _bmi_category(bmi)

    return (
        f"BMI: {bmi:.1f} ({category}). "
        "BMI is a screening estimate and does not measure body composition directly."
    )
