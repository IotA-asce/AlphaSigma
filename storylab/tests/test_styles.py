from datetime import date, timedelta

from storylab.src.styles import StyleRotator


def test_style_rotation_cycles_through_styles():
    rotator = StyleRotator(["a", "b"])
    assert rotator.get_style() == "a"
    assert rotator.get_style() == "b"
    assert rotator.get_style() == "a"


def test_style_selection_deterministic_per_date():
    rotator = StyleRotator(["a", "b", "c"])
    day = date(2024, 1, 1)
    # Repeated calls with same date yield the same style
    first = rotator.style_for_date(day)
    second = rotator.style_for_date(day)
    assert first == second

    # Dates separated by multiples of the number of styles map to same style
    repeat_day = day + timedelta(days=len(rotator.styles))
    assert rotator.style_for_date(repeat_day) == first
