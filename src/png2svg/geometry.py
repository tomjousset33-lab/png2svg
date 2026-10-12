import math


def hexagon_vertices(center_x, center_y, radius):
    """Return the six border points of a regular hexagon."""
    vertices = []
    for i in range(6):
        vertices.append(
            (
                center_x + radius * math.cos(i * math.pi / 3),
                center_y + radius * math.sin(i * math.pi / 3),
            )
        )  # return the points by using the 60 degrees angle
    return vertices
