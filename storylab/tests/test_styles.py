from storylab.src.styles import StyleRotator


def test_style_rotation_cycles_through_styles():
    rotator = StyleRotator(["a", "b"])
    assert rotator.get_style() == "a"
    assert rotator.get_style() == "b"
    assert rotator.get_style() == "a"
