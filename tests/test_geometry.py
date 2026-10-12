import math

from png2svg.geometry import hexagon_vertices


def test_hexagon_has_six_vertices():
    """Test that our function defines a six vertices hexagon."""
    vertices = hexagon_vertices(10.0, 20.0, 5.0)

    assert len(vertices) == 6


def test_hexagon_vertices_are_at_the_requested_radius():
    """Test that we keep the radius as key builder."""
    center_x, center_y, radius = 10.0, 20.0, 5.0

    vertices = hexagon_vertices(center_x, center_y, radius)

    for x, y in vertices:
        distance = math.hypot(x - center_x, y - center_y)
        assert math.isclose(distance, radius)
