from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_fourteen_year_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_fifteen_year_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_twenty_three_year_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_twenty_four_year_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_twenty_eight_year_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_dog_step_logic() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_cat_dog_boundary_values() -> None:
    assert get_human_age(27, 28) == [2, 2]
