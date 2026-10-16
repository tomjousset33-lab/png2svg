
import math

import pytest

from png2svg.grid import hexagon_centers


def test_hexagon_centers_returns_centers() -> None:
    centers = hexagon_centers(width=10, height=10, radius=2)

    assert centers
    assert centers[0] == (-2, -math.sqrt(3))


def test_adjacent_columns_are_offset_vertically() -> None:
    centers = hexagon_centers(width=10, height=10, radius=2)

    assert (1, 0) in centers
    assert (1, 2 * math.sqrt(3)) in centers


def test_same_column_has_correct_vertical_spacing() -> None:
    centers = hexagon_centers(width=10, height=10, radius=2)

    assert (-2, math.sqrt(3)) in centers
    assert (-2, 3 * math.sqrt(3)) in centers


@pytest.mark.parametrize(
    ("width", "height", "radius"),
    [(0, 10, 2), (10, 0, 2), (10, 10, 0), (-1, 10, 2)],
)
def test_invalid_dimensions_raise_value_error(
    width: int,
    height: int,
    radius: float,
) -> None:
    with pytest.raises(ValueError):
        hexagon_centers(width, height, radius)
